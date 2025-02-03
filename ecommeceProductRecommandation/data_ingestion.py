from langchain_astradb import AstraDBVectorStore
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from ecommeceProductRecommandation.data_converter import dataConverter
from config import Config
import os

embedding = HuggingFaceInferenceAPIEmbeddings(api_key= Config.HF_TOKEN, model_name="BAAI/bge-base-en-v1.5")

def data_ingestion(status):

    vstore = AstraDBVectorStore(
        embedding=embedding,
        collection_name = "RecoomandationDB",
        api_endpoint = Config.ASTRADB_API_ENDPOINT,
        token = Config.ASTRA_DB_APPLICATION_TOKEN,
        namespace = Config.ASTRADB_KEYSPACE 
    )

    storage = status

    if storage == None:
        docs = dataConverter()
        insert_ids = vstore.add_documents(docs)
    
    else:
        return vstore
    return vstore, insert_ids

if __name__ == "__main__":
    try:
        embedding_test = embedding.embed_documents(["Test text"])
        print("Embedding test result:", embedding_test)
    except Exception as e:
        print("Error testing embedding:", e)


    vstore, insert_ids = data_ingestion(None)
    print(f"\n Inserted {len(insert_ids)} documents.")
    results = vstore.similarity_search("Can you tell me the low budget sound basshead?")
    for res in results:
        print(f"\n {res.page_content} [{res.metadata}]")
    