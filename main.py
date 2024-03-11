import sys


from inSiteGpt.exception import inSiteGptException
from inSiteGpt.pipeline.pipeline import StartPipeline

def start_main():
    try:
        start_pipeline = StartPipeline()
        start_pipeline.start_pipeline()
    except Exception as e:
        raise inSiteGptException(e,sys)
    
if __name__=="__main__":
    start_main()



