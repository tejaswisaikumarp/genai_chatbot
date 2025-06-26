from flask import Flask, render_template, jsonify, request
from src.helper import huggingface_embedding_model
from langchain_pinecone import PineconeVectorStore
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import *
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

Pinecone_API=os.environ.get("PINECONE_API_KEY")
OpenAI_API=os.environ.get("OPENAI_API_KEY")

os.environ["PineconeAPIkey"]=Pinecone_API
os.environ["OpenaiAPIkey"]=OpenAI_API

embeddings=huggingface_embedding_model()

# Load the existing index from pinecone vector store
index_name = "chatbot"
load_index_vectos = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings,
)
load_index_vectos

retrieval = load_index_vectos.as_retriever(search_type='similarity', search_kwargs={"k":3})

llm = ChatOpenAI(temperature=0.2, max_tokens = 200, model='gpt-3.5-turbo')

prompt =  ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_and_answer_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
rag_chain = create_retrieval_chain(retrieval, question_and_answer_chain)

@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    message = request.form["msg"]
    input = message
    print(input)
    response = rag_chain.invoke({"input": message})
    print("Response : ", response["answer"])
    return str(response["answer"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)