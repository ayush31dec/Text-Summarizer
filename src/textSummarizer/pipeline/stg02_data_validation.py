from textSummarizer.logging import logger
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation


class DataValidationPipeline:

    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        data_validation_config = self.config.fetch_datavalidation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files_exists()
