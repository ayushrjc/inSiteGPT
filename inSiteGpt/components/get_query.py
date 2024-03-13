import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException

class Query:
    def bert_query(self,field,user_input_vector):
        try:
            logging.info("Entered into bert_query function in Query class")
            query = {
                    "field":field,
                    "query_vector": user_input_vector,
                    "k": 10,
                    "num_candidates": 500
                }
            return query
        except Exception as e:
            raise inSiteGptException(e,sys)