from llama_index.core import VectorStoreIndex
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding #new
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings

import sys
from exception import customexception
from logger import logging

def download_genai_embedding(model,document):
    """
    Downloads and initializes a GoogleGenAI gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("")
        # gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        # service_context = ServiceContext.from_defaults(llm=model,embed_model=gemini_embed_model, chunk_size=800, chunk_overlap=20)

        Settings.llm = None # Prevent LlamaIndex from trying to default to OpenAI
        Settings.embed_model = GoogleGenAIEmbedding(model_name = "text-embedding-004")
        Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
        Settings.num_output = 512
        Settings.context_window = 3900
        
        logging.info("")
        index = VectorStoreIndex.from_documents(
            document, embed_model=Settings.embed_model
        )
        index.storage_context.persist()
        
        logging.info("")
        # query_engine = index.as_query_engine(model = Settings.model)

        # Create query engine with better response behavior
        query_engine = index.as_query_engine(
            similarity_top_k=2,
            response_mode="compact",
            llm=Settings.model
        )

        return query_engine
    except Exception as e:
        raise customexception(e,sys)