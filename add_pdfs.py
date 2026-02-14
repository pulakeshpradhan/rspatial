
import os
import shutil
import difflib
from pypdf import PdfReader

def normalize(s):
    return s.lower().replace('_', ' ').replace('-', ' ').replace('.md', '').replace('.pdf', '')

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n\n### Slide {i+1}\n\n"
                text += page_text
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

def add_pdfs():
    # 1. Create docs/pdfs directory
    pdf_dir = 'docs/pdfs'
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    # 2. List all PDFs and copy them
    src_pdf_dir = 'pdf'
    if not os.path.exists(src_pdf_dir):
        print("No pdf directory found")
        return

    pdf_files = [f for f in os.listdir(src_pdf_dir) if f.lower().endswith('.pdf')]
    pdf_files_map = {f: os.path.join(src_pdf_dir, f) for f in pdf_files}
    
    for valid_pdf in pdf_files:
        shutil.copy(os.path.join(src_pdf_dir, valid_pdf), os.path.join(pdf_dir, valid_pdf))
        print(f"Copied {valid_pdf}")

    # 3. List MD files
    md_files = [f for f in os.listdir('docs') if f.endswith('.md')]

    # 4. Map and Append
    print("\nMatches and Extraction:")
    for md_file in md_files:
        if md_file == 'index.md': continue
        
        md_norm = normalize(md_file)
        
        # Remove leading numbers from md (e.g. 01 basic...)
        parts = md_norm.split(' ', 1)
        if len(parts) > 1 and parts[0].isdigit():
            md_core = parts[1]
        else:
            md_core = md_norm

        best_pdf = None
        best_score = 0
        
        for pdf in pdf_files:
            pdf_norm = normalize(pdf)
            score = difflib.SequenceMatcher(None, md_core, pdf_norm).ratio()
            
            # Boost score if words match significantly
            md_words = set(md_core.split())
            pdf_words = set(pdf_norm.split())
            common = md_words.intersection(pdf_words)
            if len(common) >= 2:
                score += 0.2
            
            if score > best_score:
                best_score = score
                best_pdf = pdf
        
        if best_score > 0.4: # Threshold
            print(f"{md_file} -> {best_pdf} ({best_score:.2f})")
            
            pdf_path = pdf_files_map[best_pdf]
            extracted_text = extract_text_from_pdf(pdf_path)
            
            # Prepare content to append
            append_content = f"\n\n## Lecture Slides Reference\n\n"
            append_content += f"[Download Slides PDF](pdfs/{best_pdf}){{ .md-button }}\n\n"
            
            if extracted_text:
                append_content += "### Extracted Slide Content\n"
                append_content += "!!! note \"Note: Text automatically extracted from slides\"\n"
                append_content += "    The following text is extracted from the presentation slides and may require formatting adjustments.\n\n"
                append_content += extracted_text
            
            with open(os.path.join('docs', md_file), 'a', encoding='utf-8') as f:
                f.write(append_content)
        else:
            print(f"{md_file} -> No match found (Best: {best_pdf} {best_score:.2f})")

if __name__ == '__main__':
    add_pdfs()
