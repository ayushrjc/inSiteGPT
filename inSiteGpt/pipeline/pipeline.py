import sys
from inSiteGpt.components.get_data import DataIngestion
from inSiteGpt.components.data_transformation import DataTransformation
from inSiteGpt.components.embeddings import DataEmbeddings
from inSiteGpt.esDB.db import ElasticsearchOperations
from inSiteGpt.components.index_mapping import IndexMapping
from inSiteGpt.components.get_query import Query
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
        self.get_query = Query()
        self.es = self.es_operations.connect()

    def start_ingest_pipeline(self):
        try:
            logging.info("Entered into Start Ingest Pipeline")
            df = self.data_ingest.get_csv()
            transformed_df = self.data_transform.transform_df(df)
            embedded_data = self.data_embedding.df_embedding_function_using_bert(transformed_df)
            vector_index_mapping = self.index_mapping.vector_index_mapping()
            self.es_operations.create_indices(es=self.es,index=index_pattern,indexMapping=vector_index_mapping)
            docs = embedded_data.to_dict("records")

            # Insert for the first time
            self.es_operations.insert_doc(es=self.es,index_pattern=index_pattern,docs=docs)
            logging.info(f"Count of records{self.es.count(index=index_pattern)}")
            
        except Exception as e:
            raise inSiteGptException(e,sys)
        
    def start_chat_pipeline(self,user_input):
            try:
                logging.info("Entered into Start Chat Pipeline")
                vector_of_user_input = self.data_embedding.user_input_embedding_function_using_bert(user_input=user_input)
                query = self.get_query.bert_query(field=field,user_input_vector=vector_of_user_input)
                results = self.es_operations.knn_search(es=self.es,query=query,index=index_pattern)
                return results
            except Exception as e:
                raise inSiteGptException(e,sys)