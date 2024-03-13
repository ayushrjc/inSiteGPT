import sys
import argparse
import streamlit as st

from inSiteGpt.exception import inSiteGptException
from inSiteGpt.pipeline.pipeline import StartPipeline



def main():
    parser = argparse.ArgumentParser(description="Start ingest pipeline or chat pipeline.")
    parser.add_argument("--ingest", action="store_true", help="Start ingest pipeline")
    # parser.add_argument("--chat", action="store_true", help="Start chat pipeline")
    args = parser.parse_args()

    if args.ingest:
        try:
            start_pipeline = StartPipeline()
            start_pipeline.start_ingest_pipeline()
        except Exception as e:
            raise inSiteGptException(e,sys)
    else:
        try:
            st.title("Search Myntra Fashion Products")
            # Input: User enters search query
            search_query = st.text_input("Enter your search query")
            # Button: User triggers the search
            if st.button("Search"):
                if search_query:
                    # Perform the search and get results
                    start_pipeline = StartPipeline()
                    results = start_pipeline.start_chat_pipeline(user_input=search_query
                                                                 )

                    # Display search results
                    st.subheader("Search Results")
                    for result in results:
                        with st.container():
                            if '_source' in result:
                                try:
                                    st.header(f"{result['_source']['ProductName']}")
                                except Exception as e:
                                    print(e)
                                
                                try:
                                    st.write(f"Description: {result['_source']['Description']}")
                                except Exception as e:
                                    print(e)

                                try:
                                    st.write(f"Price: {result['_source']['Price']}")
                                except Exception as e:
                                    print(e)
                                st.divider()

        except Exception as e:
            raise inSiteGptException(e,sys)
    # else:
    #     print("Please specify either --ingest or --chat.")
    
if __name__=="__main__":
    main()



