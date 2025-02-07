import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'src')))
#Explanation:
#sys.path.append(...): This appends the src directory (relative to the script location) to the sys.path, which is where Python looks for modules to import.
#os.path.abspath(os.path.join(...)): This generates the absolute path to the src directory.
from logger import logging

def error_message_details(error, error_detail:sys): #error_detail will be there in sys
    _, _, exc_tb=error_detail.exc_info()  #exc_tb will provide the information about why the exception has occured, which file and which line number the exception has occured, etc...
    file_name = exc_tb.tb_frame.f_code.co_filename #tb_frame, f_code and co_filename are properties. Visti custom exception handing documentation on web
    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)) 
    
    return error_message
    

#Whenever cutomeException is raised, first of all it inherits the parent exception, 
# whatever error_message is coming from the function 'error_message_details', 
# that particular message willl come over here and we will intialize it to customException variable
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) #As we are inherting from the exception
        self.error_message= error_message_details(error_message, error_detail = error_detail)
    
    def __str__(self):
        return self.error_message
