from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceBgeEmbeddings
import os 
from dotenv import load_dotenv
load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

class SearchSimilar:
    
    def setup_vector_db(chunks):
        """Setup vector database from PDF"""

        #Load the embedding model 
        model_kwargs = {"device":"cpu"}
        encode_kwargs = {"normalize_embeddings": False}
        model_name = "BAAI/bge-large-en"

        embeddings = HuggingFaceBgeEmbeddings(
            model_name = model_name,
            encode_kwargs = encode_kwargs,
            model_kwargs = model_kwargs
        )
        # Create vector database
        print("embedding model loaded succesfully......")

        url = QDRANT_URL
        collection_name = COLLECTION_NAME
        qdrant = Qdrant.from_documents(
            chunks,
            embeddings,
            url = url,
            prefer_grpc = False,
            collection_name = collection_name

        )

        print("Qdrant index created")
        # embeddings = HuggingFaceBgeEmbeddings(
        #     model_name="sentence-transformers/all-mpnet-base-v2"
        # )
        # vector_db = FAISS.from_documents(chunks, embeddings)
        
        # return vector_db

   