import os,sys
from sensor.utils import *
from sensor.logger import logging
from sensor.entity import config_entity
from sensor.entity.config_entity import *
from sensor.components import data_ingestion
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation


if __name__ == "__main__":
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        
        data_validation_config = DataValidationConfig(training_pipeline_config=training_pipeline_config)
        
        data_validation = DataValidation(data_validation_congif=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        
        data_validation_artifact = data_validation.initiate_data_validation()
        
        print(data_validation_artifact)
    except Exception as e:
        print(e)