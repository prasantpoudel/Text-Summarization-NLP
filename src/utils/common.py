import os
from box.exceptions import BoxValueError
import yaml
from src.logging import logging
from ensure import ensure_annotation
from box import configBox
from pathlib import Path
from typing import Any

@ensure_annotation
def read_yaml(path_to_yaml:Path)-> configBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info(f"yaml file:{path_to_yaml} loaded sucessfully")
            return configBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotation
def create_directories(path_to_directorries:list,verbose=True):
    for path in path_to_directorries:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"created directory at:{path}")


@ensure_annotation
def get_size(path:Path)->str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"