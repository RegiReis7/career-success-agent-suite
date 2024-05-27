from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import bedrock as embeddings
from langchain_community.vectorstores import faiss
from typing import List
import boto3
from tools.pdf_reader import read_pdf

class SearchDocument():
    
    def __init__(self, pdfFile) -> None:
        self.bedrock_client = boto3.client(
            service_name='bedrock-runtime', region_name='us-east-1')

        self.bedrock_embeddings = embeddings.BedrockEmbeddings(
            model_id="amazon.titan-embed-text-v1", client=self.bedrock_client)

        self.pdfFile = pdfFile

    def __text_splitter(self, document_text: str) -> List[str]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        return text_splitter.split_text(document_text)

    def __index(self, text_chunks) -> None:

        self.vectorstore = faiss.FAISS.from_texts(
            texts=text_chunks, embedding=self.bedrock_embeddings)

    def getRetriever(self) -> str:
        pdf_text = read_pdf(self.pdfFile)
        chunks = self.__text_splitter(pdf_text)
        self.__index(chunks)
        return self.vectorstore.as_retriever()
    
    
