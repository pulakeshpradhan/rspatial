
import os
import shutil
import difflib

def normalize(s):
    return s.lower().replace('_', ' ').replace('-', ' ').replace('.md', '').replace('.pdf', '')

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
    pdf_map = {} # filename -> full path in docs

    for valid_pdf in pdf_files:
        shutil.copy(os.path.join(src_pdf_dir, valid_pdf), os.path.join(pdf_dir, valid_pdf))
        pdf_map[valid_pdf] = f"pdfs/{valid_pdf}"
        print(f"Copied {valid_pdf}")

    # 3. List MD files
    md_files = [f for f in os.listdir('docs') if f.endswith('.md')]

    # 4. Map and Append
    # Heuristic: longest common subsequence match or keyword match
    
    for md_file in md_files:
        if md_file == 'index.md': continue
        
        best_match = None
        best_ratio = 0.0
        
        md_norm = normalize(md_file)
        # Remove leading numbers from md (e.g. 01 basic...)
        parts = md_norm.split(' ', 1)
        if len(parts) > 1 and parts[0].isdigit():
            md_core = parts[1]
        else:
            md_core = md_norm

        for pdf_file in pdf_files:
            pdf_norm = normalize(pdf_file)
            
            # Simple keyword match first
            # e.g. "numpy" in "working with numpy"
            # We use SequenceMatcher on the normalized strings
            ratio = difflib.SequenceMatcher(None, md_core, pdf_norm).ratio()
            
            # Boost if "session" number matches?
            # Creating a robust mapping is hard. Let's rely on ratio.
            
            if ratio > best_match_ratio(best_ratio):
                 best_ratio = ratio
                 best_match = pdf_file

        # Check for specific strong keywords if ratio is low?
        # Actually let's just use a threshold
        if best_match and best_ratio > 0.3: # 0.3 is low but might work for "panda" vs "pandas"
             # Refine: Check if Key words are present
             # e.g. "numpy" in md and "numpy" in pdf
             pass
             
    # Better approach: Iterate MD and finding the BEST pdf.
    # Printing matches for verification
    print("\nMatches:")
    for md_file in md_files:
        md_norm = normalize(md_file)
        best_pdf = None
        best_score = 0
        
        for pdf in pdf_files:
            pdf_norm = normalize(pdf)
            score = difflib.SequenceMatcher(None, md_norm, pdf_norm).ratio()
            if score > best_score:
                best_score = score
                best_pdf = pdf
        
        if best_score > 0.4: # Threshold
            print(f"{md_file} -> {best_pdf} ({best_score:.2f})")
            
            # Append to file
            link_text = f"\n\n## Lecture Slides\n\n[Download {best_pdf}](pdfs/{best_pdf})\n"
            # Optional: Extract text? 
            #  Skipping text extraction for now to avoid messiness, just linking.
            
            with open(os.path.join('docs', md_file), 'a', encoding='utf-8') as f:
                f.write(link_text)
        else:
            print(f"{md_file} -> No match found (Best: {best_pdf} {best_score:.2f})")

def best_match_ratio(curr):
    return curr

if __name__ == '__main__':
    add_pdfs()
