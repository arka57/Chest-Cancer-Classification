import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="classifier"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path=Path(file_path)#converting \ of windows into /
    file_dir,file_name=os.path.split(file_path)

    #creating directory if not there
    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory; {file_dir} for the file: {file_name}")

    #creating the file in memory if it doesn't exist or is an empty file
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")

    else:
        logging.info(f"{file_name} already exists")            

