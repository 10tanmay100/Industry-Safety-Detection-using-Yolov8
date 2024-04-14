import os.path
import sys
import yaml
import base64
import zipfile
import os
from zipfile import ZipFile 
from pathlib import Path

from safety.exception import safetyException
from safety.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise safetyException(e, sys) from e


def decodeImage(imgstring, fileName):
    try:
        imgdata = base64.b64decode(imgstring)
        with open("./data/" + fileName, 'wb') as f:
            f.write(imgdata)
            f.close()
    except Exception as e:
        raise safetyException(e, sys) from e


def encodeImageIntoBase64(croppedImagePath):
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())
    except Exception as e:
        raise safetyException(e, sys) from e
    

def unzip_files(source_folder, destination_folder):


    with ZipFile(source_folder, 'r') as zObject: 

        zObject.extractall( 
            path=destination_folder) 


# # Example usage
# source = 'path/to/your/source/folder'  # Replace with the path to your zip files
# destination = 'path/to/your/destination/folder'  # Replace with the path where you want to store the extracted files
# unzip_files(source, destination)
