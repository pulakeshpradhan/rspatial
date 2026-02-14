
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
    
    # 3. Define the desired structure (Manual Grouping for better UX)
    # The keys are Section Titles, values are lists of filename prefixes (without extension)
    structure = {
        "Python Fundamentals": [
            "01_Basic_Data_types",
            "02_Data_Structures_in_Python",
            "03_Functions_Loops_Controlflow",
            "04_OOP_Error_and_File_handling"
        ],
        "Data Science Core": [
            "09_Working_with_Numpy",
            "05_Working_with_Pandas_Part_I",
            "06_Working_with_Pandas_Part_II",
            "Data_Visualization_using_Python",
            "Web_Scraping_web_Table"
        ],
        "Time Series Analysis": [
            "10_Time_Series_Analysis_Part_I",
            "11_Time_Series_Analysis_Part_II"
        ],
        "Geospatial Analysis & Cloud": [
            "07_Geospatial_Analysis_Vector_Data",
            "Geospatial_Analysis_Working_with_Raster_Data",
            "OpenWeatherMapAPI",
            "Open_Meteo_WEB_API",
            "NWA_Cloud_based_Geospatial_data_processing",
            "Prediction"
        ]
    }

    # Flatten structure to get list of all known files
    known_files = []
    for section_files in structure.values():
        known_files.extend(section_files)

    # 4. Find all .ipynb files
    all_files = [f for f in os.listdir('.') if f.endswith('.ipynb')]
    files_to_convert = []
    
    # Add files from structure first to maintain order
    for base_name in known_files:
        fname = base_name + '.ipynb'
        if fname in all_files:
            files_to_convert.append(fname)
    
    # Add any remaining files to a "Miscellaneous" section if they exist
    misc_files = []
    for fname in all_files:
        if fname not in files_to_convert:
            files_to_convert.append(fname)
            misc_files.append(os.path.splitext(fname)[0])

    if misc_files:
        structure["Miscellaneous"] = misc_files

    # 5. Convert files
    print(f"Converting {len(files_to_convert)} notebooks...")
    for fname in files_to_convert:
        cmd = ['jupyter', 'nbconvert', '--to', 'markdown', '--output-dir', 'docs', fname]
        print(f"Running: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)

    # 6. Generate mkdocs.yml with navigation
    nav = [{'Home': 'index.md'}]
    
    for section, file_bases in structure.items():
        section_nav = []
        for base in file_bases:
            # Check if file actually exists (some might be missing or renamed)
            if base + '.ipynb' in all_files:
                title = base.replace('_', ' ').replace('-', ' ')
                # Remove leading numbers for cleaner titles (optional, user pref?)
                # keeping numbers helps ordering logic if relevant
                section_nav.append({title: base + '.md'})
        
        if section_nav:
            nav.append({section: section_nav})

    mkdocs_config = {
        'site_name': 'GeoPython Tutorial',
        'theme': {
            'name': 'material',
            'features': [
                'navigation.tabs',
                'navigation.sections',
                'toc.integrate'
            ],
            'palette': [
                {'scheme': 'default', 'primary': 'teal', 'accent': 'purple'},
                {'scheme': 'slate', 'primary': 'teal', 'accent': 'lime'}
            ]
        },
        'nav': nav,
        'plugins': ['search'],
        'markdown_extensions': [
            'admonition',
            'pymdownx.details',
            'pymdownx.superfences'
        ]
    }

    with open('mkdocs.yml', 'w') as f:
        yaml.dump(mkdocs_config, f, sort_keys=False)
    print("Generated mkdocs.yml")

if __name__ == '__main__':
    setup_mkdocs()
