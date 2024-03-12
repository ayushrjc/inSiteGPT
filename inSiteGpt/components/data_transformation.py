import pandas as pd
import numpy as np
import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException


class DataTransformation:
    def transform_df(self,df):
        try:
            logging.info("Entered into Data transform_df function in DataTransfomation class")
            logging.info("Dropping N/A")
            df.dropna(inplace=True)
            logging.info(f"Shape of df: {df.shape}")
            logging.info("New column 'NameDescription' added")
            df["NameDescription"] = df["ProductName"] + df["Description"]
            logging.info(f"df: {df.head(2)}")
            return df

        except Exception as e:
            raise inSiteGptException(e,sys)