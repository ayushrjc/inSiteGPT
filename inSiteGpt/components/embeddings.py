import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException

class DataEmbeddings:
    def embedding_function(self,df):
        try:
            # return embadded df with df['embedded_column']
            return df
        except Exception as e:
            raise inSiteGptException(e,sys)
        
    #sample code using OpenAI
        
'''
from openai import OpenAI
client = OpenAI(api_key="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")

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

df['ada_embedding'] = df.combined.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
'''