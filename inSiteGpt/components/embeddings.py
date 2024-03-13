import sys
from inSiteGpt.logger import logging
from inSiteGpt.exception import inSiteGptException
from inSiteGpt.embedding_models.bert_embedding import BertDataEmbeddings

class DataEmbeddings:
    def __init__(self):
        self.bert_emb_obj = BertDataEmbeddings()

    def df_embedding_function_using_bert(self,df):
        try:
            df=self.bert_emb_obj.df_embedding(df)
            return df
        except Exception as e:
            raise inSiteGptException(e,sys)
    def user_input_embedding_function_using_bert(self,user_input):
        try:
            vector_of_user_input=self.bert_emb_obj.user_input_embedding(user_input)
            return vector_of_user_input
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