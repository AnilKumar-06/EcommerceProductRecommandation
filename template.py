import os
from pathlib import Path

project_name = "ecom_recommandation"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/data_converter.py",
    f"{project_name}/data_ingestion.py",
    f"{project_name}/retrieval_generation.py",
    "static/style.css",
    "app.py",
    "setup.py",
    "requirements.txt",
    ".env",
]

for fpath in list_of_files:
    fpath = Path(fpath)
    fdir, fname = os.path.split(fpath)

    if fdir !="":
        os.makedirs(fdir, exist_ok=True)
    if (not os.path.exists(fname)) or (os.path.getsize(fpath)==0):
        with open(fpath, "w") as f:
            pass