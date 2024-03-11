import pandas as pd
import numpy as np
import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException


class DataIngestion:
    def get_csv(self):
        try:
            logging.info("Importing csv file")
            df = pd.read_csv("myntra_products_catalog.csv")[:500]
            df.dropna(inplace=True)
            logging.info("Shape of df: ",df.shape)
        except Exception as e:
            raise inSiteGptException(e,sys)