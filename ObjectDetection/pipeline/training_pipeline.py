import sys, os
from ObjectDetection.logger import logging
from ObjectDetection.exception import AppException
from ObjectDetection.components.data_ingestion import DataIngestion
from ObjectDetection.components.data_validation import DataValidation

from ObjectDetection.entity.config_entity import (DataIngestionConfig,
                                                  DataValidationConfig)

from ObjectDetection.entity.artifacts_entity import (DataIngestionArtifacts,
                                                     DataValidationArtifact)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()


    def start_data_ingestion(self)-> DataIngestionArtifacts:
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config
            )

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifacts
        
        except Exception as e:
            raise AppException(e,sys)
        
    def start_data_validation(
            self, data_ingestion_artifact: DataIngestionArtifacts
    ) -> DataValidationArtifact:
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")

            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )
            return data_validation_artifact
        except Exception as e:
            raise AppException(e,sys) from e
        

    def run_pipeline(self)-> None:
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifacts
            )

        except Exception as e:
            raise AppException(e,sys)