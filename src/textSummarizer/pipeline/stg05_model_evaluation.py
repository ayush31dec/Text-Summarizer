from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logging
from textSummarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    """
    Model Evaluation Pipeline
    """
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        model_evaluation_config = self.config.fetch_modelevaluation_config()
        model_evaluation_config = ModelEvaluation(model_evaluation_config)
        model_evaluation_config.evaluate()
