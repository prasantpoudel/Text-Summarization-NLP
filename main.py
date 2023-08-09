from src.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.pipeline.stage_o4_model_training import ModelTrainerPipeline
from src.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from src.logging import logging


STAGE_NAME="Data Ingestion Stage"
try:
    logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f" {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"
try:
    logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_Validation=DataValidationTrainingPipeline()
    data_Validation.main()
    logging.info(f" {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"
try:
    logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_Transformation=DataTransformationPipeline()
    data_Transformation.main()
    logging.info(f" {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME="Model Training Stage"
try:
    logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    model_training=ModelTrainerPipeline()
    model_training.main()
    logging.info(f" {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME="Model Evaluation Stage"
try:
    logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    model_evaluation=ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info(f" {STAGE_NAME} Completed")
except Exception as e:
    logging.exception(e)
    raise e

