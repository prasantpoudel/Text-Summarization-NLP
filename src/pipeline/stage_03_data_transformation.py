from src.config.configuration import ConfigurationManger
from src.components.data_transformation import DataTransformation
from src.logging import logging

class DataTransformationPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()