import pandas as pd
import numpy as np
import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException
from inSiteGpt.constants import data_path

class DataIngestion:
    def get_csv(self):
        try:
            logging.info("Importing csv file")
            df = pd.read_csv(data_path+"myntra_products_catalog.csv")[:500]
            return df 
        
        except Exception as e:
            raise inSiteGptException(e,sys)
        
    