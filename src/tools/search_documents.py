from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import bedrock as embeddings
from langchain_community.vectorstores import faiss
from typing import List
import boto3
from crewai_tools import tool
from tools.pdf_reader import read_pdf


class SeachDocument():

    def __init__(self, pdfFile) -> None:
        self.__bedrock_client = boto3.client(
            service_name='bedrock-runtime', region_name='us-east-1')

        self.__bedrock_embeddings = embeddings.BedrockEmbeddings(
            model_id="amazon.titan-embed-text-v1", client=self.__bedrock_client)

        self.__pdfFile = pdfFile

    def __text_splitter(self, document_text: str) -> List[str]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        return text_splitter.split_text(document_text)

    def __index(self, text_chunks) -> None:

        self.__vectorstore = faiss.FAISS.from_texts(
            texts=text_chunks, embedding=self.__bedrock_embeddings)

    @tool("Document Search Engine")
    def search_document(self, query: str) -> str:
        """Search through a document and retrieve the most relevant pieces based on the query"""
        pdf_text = read_pdf(self.__pdfFile)
        chunks = self.__text_splitter(pdf_text)
        self.__index(chunks)
        search_results = self.__vectorstore.similarity_search(query, k=1)
        return search_results[0].page_content()
