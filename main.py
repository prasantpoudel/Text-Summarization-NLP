from src.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
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