import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # helps you create classes mainly to store data

# for taking input files
@dataclass # Decorator = a tool that adds extra behavior to a function or method without changing its code.
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    # artifacts folder will contain all the files created during the pipeline run

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self): # to read data from databases
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv('notebook/data/stud.csv') # here we read the data we can add path from mongodb etc also.
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            # to make sure artifacts folder is created
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")
            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path,
                    self.ingestion_config.raw_data_path)

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__": 
    obj = DataIngestion()
    obj.initiate_data_ingestion()


