from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionPipeline:
    def __init__(self) -> None:
        self.config = ConfigurationManager()

    def main(self):
        
        data_ingestion_config = self.config.fetch_dataingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()
