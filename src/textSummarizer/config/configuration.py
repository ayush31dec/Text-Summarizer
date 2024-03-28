from textSummarizer.constants import *
from textSummarizer.utils.common_utils import read_yaml, create_directories
from textSummarizer.entities import (DataIngestionConfig, DataValidationConfig)

class ConfigurationManager:

    def __init__(
            self,
            config_file_path=CONFIG_FILE_PATH,
            params_file_path=PARAMS_FILE_PATH
            ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def fetch_dataingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_filepath=config.local_data_filepath,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def fetch_datavalidation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_filepath=config.status_filepath,
            all_required_files=config.all_required_files
        )

        return data_validation_config
