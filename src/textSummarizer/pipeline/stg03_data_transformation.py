from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    """
    Data Transformation Pipeline
    """
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        data_transformation_config = self.config.fetch_datatransformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.convert()