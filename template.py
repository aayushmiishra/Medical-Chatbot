# will creat project template 
import os #provides function to intetract with the operating system
from pathlib import Path #object oriented way to work with file paths
import logging #use to display log messages(info, error, warning, etc.)

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s') #sets up logging so that each message has a timestamp

list_of_files = [
    "src/__init__.py",
    "src/helpers.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass  
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
