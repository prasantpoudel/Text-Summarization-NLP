from src.config.configuration import ConfigurationManger
from src.components.model_evaluation import ModelEvaluation
from src.logging import logging

class ModelEvaluationPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()