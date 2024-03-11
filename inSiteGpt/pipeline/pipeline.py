import sys
from inSiteGpt.components.get_data import DataIngestion
from inSiteGpt.components.data_transformation import DataTransformation
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException

class StartPipeline:
    def __init__(self):
        self.data_ingest = DataIngestion()
        self.data_transform = DataTransformation()

    def start_pipeline(self):
        try:
            logging.info("Entered into StartPipeline Class")
            df = self.data_ingest.get_csv()
            transformed_df = self.data_transform.transform_df(df)

        except Exception as e:
            raise inSiteGptException(e,sys)
