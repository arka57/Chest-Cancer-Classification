#from src.classifier import logger
from classifier import logger
from classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        ob=DataIngestionTrainingPipeline()
        ob.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
        raise e    