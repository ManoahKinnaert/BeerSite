from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.retrievers.ensemble import EnsembleRetriever
from langchain.retrievers import BM25Retriever
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_ollama.chat_models import ChatOllama
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file using PyMuPDF."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def process_document(file_path):
    """Process the PDF and split the text into chunks."""
    text = extract_text_from_pdf(file_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_text(text)

def create_hybrid_retriever(chunks):
    """Create a hybrid retriever using vector + BM25 retrieval."""
    vector_store = Chroma.from_texts(
        chunks,
        OllamaEmbeddings(model="llama3")
    )

    bm25 = BM25Retriever.from_texts(chunks)
    bm25.k = 2

    return EnsembleRetriever(
        retrievers=[
            vector_store.as_retriever(search_kwargs={"k": 3}),
            bm25
        ],
        weights=[0.6, 0.4]
    )

def initialize_conversation(retriever):
    import os
    """Initialize conversational retrieval chain."""
    llm = ChatOllama(model="llama3", temperature=0.7, base_url=f"http://{os.environ["OLLAMA_HOST"]}")

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key='answer' 
        ),
        chain_type="stuff",
        return_source_documents=True
    )