import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException
from sentence_transformers import SentenceTransformer

class BertDataEmbeddings:
    def embedding(self,df):
        try:
            logging.info("Entered into embedding function in BertDataEmbeddings class")
            model = SentenceTransformer('all-mpnet-base-v2')
            if "NameDescription" in df.columns:
                df["NameDescriptionVector"] = df["NameDescription"].apply(lambda x: model.encode(x))
                logging.info(f"df: {df.head(2)}")
            return df
        except Exception as e:
            raise inSiteGptException(e,sys)