import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException

class IndexMapping:
    def sample_index_mapping(self):
        try:
            indexMapping = {
                "properties":{
                    "ProductID":{
                        "type":"long"
                    },
                    "ProductName":{
                        "type":"text"
                    },
                    "ProductBrand":{
                        "type":"text"
                    },
                    "Gender":{
                        "type":"text"
                    },
                    "Price (INR)":{
                        "type":"long"
                    },
                    "NumImages":{
                        "type":"long"
                    },
                    "Description":{
                        "type":"text"
                    },
                    "PrimaryColor":{
                        "type":"text"
                    },
                    "NameDescription":{
                        "type":"text"
                    }

                }
            }
            return indexMapping

        except Exception as e:
            raise inSiteGptException(e,sys)
    
    def vector_index_mapping(self):
        try:
            indexMapping = {
                "properties":{
                    "ProductID":{
                        "type":"long"
                    },
                    "ProductName":{
                        "type":"text"
                    },
                    "ProductBrand":{
                        "type":"text"
                    },
                    "Gender":{
                        "type":"text"
                    },
                    "Price (INR)":{
                        "type":"long"
                    },
                    "NumImages":{
                        "type":"long"
                    },
                    "Description":{
                        "type":"text"
                    },
                    "PrimaryColor":{
                        "type":"text"
                    },
                    "NameDescription":{
                        "type":"text"
                    },
                    "NameDescriptionVector":{
                        "type":"dense_vector",
                        "dims": 1536,
                        "index":True,
                        "similarity": "l2_norm"
                    }

                }
            }
            return indexMapping

        except Exception as e:
            raise inSiteGptException(e,sys)

