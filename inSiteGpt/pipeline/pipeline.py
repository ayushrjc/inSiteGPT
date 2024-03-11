import sys
from inSiteGpt.components.get_data import DataIngestion
from inSiteGpt.components.data_transformation import DataTransformation
from inSiteGpt.components.embeddings import DataEmbeddings
from inSiteGpt.esDB.db import ElasticsearchOperations
from inSiteGpt.components.index_mapping import IndexMapping
from inSiteGpt.constants import *
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException

class StartPipeline:
    def __init__(self):
        self.data_ingest = DataIngestion()
        self.data_transform = DataTransformation()
        self.data_embedding = DataEmbeddings()
        self.es_operations = ElasticsearchOperations()
        self.index_mapping = IndexMapping()

    def start_pipeline(self):
        try:
            logging.info("Entered into StartPipeline Class")
            df = self.data_ingest.get_csv()
            transformed_df = self.data_transform.transform_df(df)
            embedded_data = self.data_embedding.embedding_function(transformed_df)
            es = self.es_operations.connect()
            sample_index_mapping = self.index_mapping.sample_index_mapping()
            self.es_operations.create_indices(es=es,index=index_pattern,indexMapping=sample_index_mapping)
            docs = embedded_data.to_dict("records")
            self.es_operations.insert_doc(es=es,index_pattern=index_pattern,docs=docs)
            logging.info(f"{es.count(index=index_pattern)}")
            
        except Exception as e:
            raise inSiteGptException(e,sys)
