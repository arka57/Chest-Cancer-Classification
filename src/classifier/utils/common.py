import os
from box.exceptions import BoxValueError #for handling exceptions
import yaml
from classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) ->ConfigBox:
    """reads yaml file and returns it

    Args:
        path_to_yaml(str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file            
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e    

@ensure_annotations
def create_directories(path_to_directories,verbose=True):
    """create list of directories

    Args:
        path_to_directories(list):list of path of directories
        ignore_log(bool,optional):ignore if multiple dirs is to be created. Defaults to false.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            print(f"created directory at : {path}")

@ensure_annotations
def get_size(path: Path)-> str:
    """get size in KB
    
    Args:
        path(Path): path of the  file
        
    Returns:
        str: size in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"                
    

@ensure_annotations
def save_json(path: Path,data: dict):
    """Save JSON data
    
    Args:
    path(Path): path to json file
    data(dict): data to be saved in json file
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at: {path}")    




def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())