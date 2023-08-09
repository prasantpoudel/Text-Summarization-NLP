from src.config.configuration import ConfigurationManger
from src.components.model_trainer import ModelTrainer
from src.logging import logging

class ModelTrainerPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()