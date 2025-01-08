import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'src')))
#Explanation:
#sys.path.append(...): This appends the src directory (relative to the script location) to the sys.path, which is where Python looks for modules to import.
#os.path.abspath(os.path.join(...)): This generates the absolute path to the src directory.

from exception import CustomException
from logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Any input which is required, we will give it through 'DataIngestionConfig' class
@dataclass
class DataIngestionConfig: 
    train_data_path: str=os.path.join('artifacts', "train.csv") #data ingestion component output will be save all the files in this path
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts', "raw.csv")
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()
        
    def inititate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) #getting the directory name w.r.t this specific path
            #exist ok = True indicates that if file/folder already exist, then please do not create new one, just keep appending
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")
            train_set, test_set= train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    obj.inititate_data_ingestion()