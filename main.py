#from src.classifier import logger
from classifier import logger
from classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from classifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from classifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
STAGE_NAME="Data Ingestion Stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        ob=DataIngestionTrainingPipeline()
        ob.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
        raise e    


STAGE_NAME="Prepare base model"

try:
        logger.info(f"**********")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj= PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Model Training"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        ob=ModelTrainingPipeline()
        ob.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
        raise e


STAGE_NAME="Evaluation Stage"

try:
        logger.info(f"**********")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj= EvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")

except Exception as e:
        logger.exception(e)
        raise e 