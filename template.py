import os

def create_file(filepath, content=""):
    """
    Create a file with the given content.
    """
    with open(filepath, "w") as file:
        file.write(content)


def create_project_structure(base_dir):
    """
    Create the project structure for the cover-identification system.
    """
    # Define the folder structure and files to create
    structure = {
        "app": [
            "__init__.py",
            "api.py",
            "utils.py",
            "preprocessing.py",
            "embedding.py",
            "transcription.py",
            "retrieval.py"
        ],
        "config": ["config.yaml"],
        "data": [
            "song_lyrics.csv",
            "top_song_lyrics.csv",
            "vector_index.faiss"
        ],
        "notebooks": ["exploratory_analysis.ipynb"],
        "logs": ["app.log"],
        "tests": ["test_utils.py", "test_endpoints.py"],
    }
    files_to_create = [
        "requirements.txt",
        "Dockerfile",
        "README.md",
        "main.py",
    ]

    # Create the folders and files
    for folder, files in structure.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            create_file(os.path.join(folder_path, file))

    # Create top-level files
    for file in files_to_create:
        create_file(os.path.join(base_dir, file), content="")

    print(f"Project structure created at: {base_dir}")


# Usage
project_name = "cover-identification"
create_project_structure(project_name)
