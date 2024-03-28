import os
import urllib.request as request
from pathlib import Path
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common_utils import get_size
from textSummarizer.entities import DataIngestionConfig

class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):

        if not os.path.exists(self.config.local_data_filepath):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_filepath
            )
            logger.info(f"{filename} downlaoded with folllowing information: \n{headers}")

        else:
            logger.info(f"file already exists of size: \n{get_size(Path(self.config.local_data_filepath))}")

    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_filepath, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)