import os
import glob

parent_dir = os.getcwd()
repo_name = 'MFE1'
default_branch = 'main'

for dir in [f"{parent_dir}"]:
    local_repo_path = os.path.join(os.path.expanduser(dir))
    print(f"Checking out {repo_name} to {local_repo_path}")

    all_globs = [
        os.path.join("**", "en-*.json"),
        os.path.join("**", "en-*", ""),
        os.path.join("**", "Resources.en-*.resx"),
        os.path.join("**", "Strings.en-*.resx"),
        os.path.join("**", "en.json"),
        os.path.join("**", "en", "*.json"),
        os.path.join("**", "Resources.resx"),
        os.path.join("**", "Strings.resx"),
        os.path.join("config", "locales", "en", "**", "*.yml"),
        os.path.join("**", "config", "locales", "en", "**", "*.yml"),
        os.path.join("**", "src", "main", "res", "values", "strings.xml"),
        os.path.join("**", "en.json"),
    ]

    translation_files = []
    for pattern in all_globs:
        translation_files.extend(glob.glob(pattern, recursive=True))
    
    translation_files = list(set(translation_files))

    print(translation_files)