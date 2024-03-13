import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException
from elasticsearch import Elasticsearch

class ElasticsearchOperations:
    def connect(self):
        try:
            logging.info("Entered into connect function in ElasticsearchOperations class")
            es = Elasticsearch(
                "http://localhost:9200"
            )
            logging.info(f"Conenction established: {es.ping()}")
            return es

        except Exception as e:
            raise inSiteGptException(e,sys)
        
    def create_indices(self,es,index,indexMapping):
        try:
            if es.indices.exists(index=index):
                pass
            else:
                logging.info("Entered into create_indices function in ElasticsearchOperations class")
                es.indices.create(index=index, mappings=indexMapping)

        except Exception as e:
            raise inSiteGptException(e,sys)
        
    def insert_doc(self,es,index_pattern,docs):
        logging.info("Entered into insert_doc function in ElasticsearchOperations class")
        for doc in docs:
            try:
                es.index(index=index_pattern, document=doc, id=doc["ProductID"])
            except Exception as e:
                raise inSiteGptException(e,sys)
            
    def knn_search(self,es,query,index):
        try:
            logging.info("Entered into knn_search function in ElasticsearchOperations class")
            res = es.knn_search(index=index
                        , knn=query 
                        , source=["ProductName","Description"]
                        )
            results = res["hits"]["hits"]
            return results

        except Exception as e:
            raise inSiteGptException(e,sys)