from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.config.configuration import ConfigurationManager


class ModelTrainerPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        model_trainer_config = self.config.fetch_modeltrainer_config()
        model_trainer_config = ModelTrainer(model_trainer_config)
        model_trainer_config.train()