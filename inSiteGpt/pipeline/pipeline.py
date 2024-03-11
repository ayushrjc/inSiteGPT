import sys
from inSiteGpt.components.get_data import DataIngestion
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException

class StartPipeline:
    def __init__(self):
        self.data_ingest = DataIngestion()

    def start_pipeline(self):
        try:
            logging.info("Entered into StartPipeline Class")
            self.data_ingest.get_csv()

        except Exception as e:
            raise inSiteGptException(e,sys)
