from classifier.config.configuration import ConfigurationManager
from classifier.components.model_trainer import Training
from classifier import logger
STAGE_NAME="Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config= ConfigurationManager()
            training_config=config.get_training_config()
            training=Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()

        except Exception as e:
            raise e


if __name__=='__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        ob=ModelTrainingPipeline()
        ob.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

    except Exception as e:
        raise e    