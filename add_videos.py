
import os
import yaml

# Video IDs provided by user
video_ids = [
    "iDWyJcB1FMo",
    "XtHkTYjH27U", 
    "_fbx9BH7qHQ", 
    "OgJGIBbDUfI", 
    "URDTyIrD5Pg", 
    "l3Hc7lS51zY", 
    "Vg-2ghjeL60", 
    "QMkQ_MgmkMw", 
    "vHaJttWUCNg", 
    "-KF71FwBA1Y", 
    "qXsdgTGwqZ0", 
    "3JHdxtNQbv8", 
    "iqPzPXMox0w", 
    "njfa48cIM9c"
]

def add_videos():
    # 1. Get file list in order from _toc.yml
    toc_files = []
    if os.path.exists('_toc.yml'):
        with open('_toc.yml', 'r') as f:
            toc_data = yaml.safe_load(f)
            if 'chapters' in toc_data:
                for chapter in toc_data['chapters']:
                    if 'file' in chapter:
                        toc_files.append(chapter['file'])
    
    # 2. Map videos to files
    mappings = []
    for i, file_base in enumerate(toc_files):
        if i < len(video_ids):
            mappings.append((file_base, video_ids[i]))
    
    # 3. Append iframe to each mapped file
    for file_base, vid_id in mappings:
        file_path = f"docs/{file_base}.md"
        if os.path.exists(file_path):
            iframe_html = f'\n\n<iframe width="560" height="315" src="https://www.youtube.com/embed/{vid_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>\n'
            
            # Read content to check if already present? (Optional, but good practice)
            # Just append for now
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(iframe_html)
            print(f"Added video {vid_id} to {file_path}")
        else:
            print(f"Warning: File {file_path} not found")

if __name__ == '__main__':
    add_videos()
