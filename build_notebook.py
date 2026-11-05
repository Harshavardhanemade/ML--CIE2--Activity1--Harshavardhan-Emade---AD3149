from pathlib import Path
import nbformat
from nbclient import NotebookClient

notebook_path = Path("dataset_preparation.ipynb")
notebook = nbformat.read(notebook_path, as_version=4)
NotebookClient(notebook, timeout=600, kernel_name="python3").execute()
nbformat.write(notebook, notebook_path)
print("Notebook executed successfully.")
