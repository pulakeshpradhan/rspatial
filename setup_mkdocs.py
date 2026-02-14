
import os
import shutil
import subprocess
import yaml

def setup_mkdocs():
    # 1. Create directory
    if not os.path.exists('docs'):
        os.makedirs('docs')

    # 2. Copy intro.md
    if os.path.exists('intro.md'):
        shutil.copy('intro.md', 'docs/index.md')
        print("Copied intro.md to docs/index.md")

    # 3. Read _toc.yml for order
    toc_files = []
    if os.path.exists('_toc.yml'):
        with open('_toc.yml', 'r') as f:
            toc_data = yaml.safe_load(f)
            # TOC structure: root: intro, chapters: list of dicts with file key
            if 'chapters' in toc_data:
                for chapter in toc_data['chapters']:
                    if 'file' in chapter:
                        toc_files.append(chapter['file'])
    
    # 4. Find all .ipynb files
    all_files = [f for f in os.listdir('.') if f.endswith('.ipynb')]
    files_to_convert = []
    
    # Prioritize TOC files
    for base_name in toc_files:
        fname = base_name + '.ipynb'
        if fname in all_files:
            files_to_convert.append(fname)
    
    # Add any remaining files
    for fname in all_files:
        if fname not in files_to_convert:
            files_to_convert.append(fname)

    # 5. Convert files
    print(f"Converting {len(files_to_convert)} notebooks...")
    for fname in files_to_convert:
        cmd = ['jupyter', 'nbconvert', '--to', 'markdown', '--output-dir', 'docs', fname]
        print(f"Running: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)

    # 6. Generate mkdocs.yml
    nav = [{'Home': 'index.md'}]
    for fname in files_to_convert:
        base_name = os.path.splitext(fname)[0]
        md_name = base_name + '.md'
        # Format title (replace _ with space)
        title = base_name.replace('_', ' ')
        nav.append({title: md_name})

    mkdocs_config = {
        'site_name': 'GeoPython Tutorial',
        'theme': {'name': 'material'},
        'nav': nav,
        'plugins': ['search']
    }

    with open('mkdocs.yml', 'w') as f:
        yaml.dump(mkdocs_config, f, sort_keys=False)
    print("Generated mkdocs.yml")

if __name__ == '__main__':
    setup_mkdocs()
