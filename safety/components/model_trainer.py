import os,sys
import yaml
from safety.utils.main_utils import read_yaml_file
from six.moves import urllib
from safety.logger import logging
from safety.exception import safetyException
from safety.entity.artifacts_entity import DataIngestionArtifact
from safety.constant.training_pipeline import *
from safety.entity.config_entity import ModelTrainerConfig
from safety.entity.artifacts_entity import ModelTrainerArtifact
from ultralytics import YOLO



class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
        ingestion_artifact:DataIngestionArtifact
    ):
        self.model_trainer_config = model_trainer_config
        self.ingestion_artifact = ingestion_artifact

    
    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try: 

            model = YOLO('yolov8s.pt')

            results = model.train(data=YAML_PATH,epochs=self.model_trainer_config.no_epochs,patience=10,save=True,save_period=-1,project='model')


            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="model/train/weights/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact






        except Exception as e:
            raise safetyException(e, sys)

