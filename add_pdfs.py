
import os
import shutil
import difflib
import re
from pypdf import PdfReader

def normalize(s):
    return s.lower().replace('_', ' ').replace('-', ' ').replace('.md', '').replace('.pdf', '')

def clean_text_chunk(text):
    # Remove common headers/footers patterns
    # e.g. "22-09-2022", single digits on a line (page numbers)
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Skip likely page numbers (just digits)
        if line.isdigit() and len(line) < 4:
            continue
            
        # Skip date-like strings (simple check)
        if re.match(r'\d{2}-\d{2}-\d{4}', line):
            continue
            
        cleaned_lines.append(line)
        
    return "\n".join(cleaned_lines)

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        full_text = []
        
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                cleaned = clean_text_chunk(page_text)
                full_text.append(cleaned)
        
        # Join all pages with double indentation
        combined_text = "\n\n".join(full_text)
        
        # Basic cleanup of broken sentences?
        # This is risky without advanced NLP, so let's stick to clean paragraphs.
        
        return combined_text
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
            # Continuous flow, professional look
            
            append_content = f"\n\n## Lecture Visualization\n\n"
            
            # Embed PDF
            append_content += f'<embed src="pdfs/{best_pdf}" type="application/pdf" width="100%" height="600px" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />\n\n'
            
            # Download Button centered or aligned
            append_content += f'<p align="center"><a href="pdfs/{best_pdf}" class="md-button md-button--primary">Download Lecture Slides</a></p>\n\n'
            
            if extracted_text:
                # Use a collapsible details block for the full text to keep page clean
                append_content += "??? info \"View Full Lecture Transcript\"\n"
                append_content += "    The following content is extracted from the lecture slides.\n\n"
                
                # Format text as a continuous block
                # Split by newlines and reconstruct to look more like paragraphs
                # We need consistent indentation for the admonition block (4 spaces)
                
                lines = extracted_text.split('\n')
                for line in lines:
                    if line.strip():
                        append_content += f"    {line.strip()}\n\n"
            
            with open(os.path.join('docs', md_file), 'a', encoding='utf-8') as f:
                f.write(append_content)
        else:
            print(f"{md_file} -> No match found (Best: {best_pdf} {best_score:.2f})")

if __name__ == '__main__':
    add_pdfs()
