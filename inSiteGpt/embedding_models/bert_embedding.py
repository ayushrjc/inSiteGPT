import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException
from sentence_transformers import SentenceTransformer

class BertDataEmbeddings:
    def __init__(self) :
        self.model = SentenceTransformer('all-mpnet-base-v2')

    def df_embedding(self,df):
        try:
            logging.info("Entered into embedding function in BertDataEmbeddings class")
            
            if "NameDescription" in df.columns:
                df["NameDescriptionVector"] = df["NameDescription"].apply(lambda x: self.model.encode(x))
                logging.info(f"df: {df.head(2)}")
            return df
        except Exception as e:
            raise inSiteGptException(e,sys)
        
    def user_input_embedding(self,user_input):
        try:
            logging.info("Entered into user_input_embedding function in BertDataEmbeddings class")
            vector_of_user_input = self.model.encode(user_input)
            return vector_of_user_input
        except Exception as e:
            raise inSiteGptException(e,sys)