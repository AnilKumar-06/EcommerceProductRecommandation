import pandas as pd
from langchain_core.documents import Document

def dataConverter():
    # Load product data
    product_data = pd.read_csv(r"C:/Users/CRRao AIMSCS/Documents/GenAI/EcommerceProductRecommandation/data/product_review.csv")
    
    # Select only relevant columns
    data = product_data[["product_title", "review"]].dropna()  # Removes rows with missing values
    print(data.head())  # Debugging output

    # Convert DataFrame to list of dictionaries (efficient method)
    product_list = data.to_dict(orient="records")

    # Convert to LangChain Document objects
    docs = [
        Document(page_content=entry["review"], metadata={"product_name": entry["product_title"]})
        for entry in product_list
    ]

    return docs