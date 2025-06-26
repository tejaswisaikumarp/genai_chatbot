from src.helper import load_pdf_file, text_split, huggingface_embedding_model
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os

from dotenv import load_dotenv
load_dotenv()

Pinecone_API=os.environ.get("PINECONE_API_KEY")
os.environ["PineconeAPIkey"]=Pinecone_API

data_extraction=load_pdf_file(data='Data/')
text_chunks=text_split(data_extraction)
embeddings=huggingface_embedding_model()

# creating an index in the pinecone vector base
pc = Pinecone(api_key=Pinecone_API)

index_name = "chatbot"

pc.create_index(name=index_name, 
                dimension=384, 
                metric='cosine', 
                spec=ServerlessSpec(cloud='aws',
                                    region='us-east-1'
                                    )
)

# Convert each chunk into a vector and store it in the index
vectors = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)