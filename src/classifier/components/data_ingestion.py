import os
import zipfile
import gdown
from classifier import logger
from classifier.utils.common import get_size
from classifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config=config


    

    def extract_zip_file(self):
        """
        Extracts zip file into the data directory
        Method returns none
        """

        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)    