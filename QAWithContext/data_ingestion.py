import sys
import os
import tempfile
from llama_index.core import Document
from logger import logging
from exception import customexception

from PyPDF2 import PdfReader  # pip install PyPDF2


def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        raise Exception(f"Failed to read PDF: {str(e)}")


def extract_text_from_txt(uploaded_file):
    try:
        return uploaded_file.read().decode("utf-8")
    except Exception as e:
        raise Exception(f"Failed to read TXT file: {str(e)}")


def load_data(uploaded_file):
    try:
        logging.info("Starting data ingestion...")

        if uploaded_file is None:
            raise ValueError("No file uploaded")

        filename = uploaded_file.name.lower()

        if filename.endswith(".pdf"):
            logging.info("PDF file detected")
            file_content = extract_text_from_pdf(uploaded_file)

        elif filename.endswith(".txt"):
            logging.info("Text file detected")
            file_content = extract_text_from_txt(uploaded_file)

        else:
            raise ValueError("Unsupported file type. Only .txt and .pdf are supported.")

        documents = [Document(text=file_content)]

        logging.info("Document successfully loaded and wrapped.")
        return documents

    except Exception as e:
        logging.error("Exception during data ingestion")
        raise customexception(e, sys)


#Alternate method : only for .txt
# from llama_index.core import SimpleDirectoryReader
# import sys
# from exception import customexception
# from logger import logging

# def load_data(doc):
#     """
#     Load PDF documents from a specified directory.

#     Parameters:
#     - data (str): The path to the directory containing PDF files.

#     Returns:
#     - A list of loaded PDF documents. The specific type of documents may vary.
#     """
#     try:
#         logging.info("data loading started...")
#         loader = SimpleDirectoryReader("Data")
#         documents=loader.load_data()
#         logging.info("data loading completed...")
#         return documents
#     except Exception as e:
#         logging.info("exception in loading data...")
#         raise customexception(e,sys)