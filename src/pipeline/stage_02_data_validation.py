from src.config.configuration import ConfigurationManger
from src.components.data_validation import DataValidation
from src.logging import logging

class DataValidationTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManger()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exists()