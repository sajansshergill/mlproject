import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #text file where these are the naming convention using which file will be named
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) #initially the "logs" mean logs/then the naming conventions
os.makedirs(logs_path, exist_ok= True) #Even though there is a file or folder, keep on appending the files whenever we want to create the file

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) 

# Wherever logging.INFO or 'import loggin' or write out any print message then it is going to use the below kind of basicConfig:
# 1. Create this file path in the format
logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO

)

if __name__ =="__main__":
    logging.info("Logging has started...")