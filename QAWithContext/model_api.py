import os
from dotenv import load_dotenv
import sys

from llama_index.llms.google_genai import GoogleGenAI #new
import google.generativeai as genai
from exception import customexception
from logger import logging
from llama_index.core import Settings

# from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display



load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini model for natural language processing.

    Returns:
    example - 
    - Gemini: An instance of the Gemini class initialized with the 'gemini-2.5-flash-lite-preview-06-17' model.
    """
    try:
        logging.info("Loading Gemini model...")
        Settings.model = GoogleGenAI(model="gemini-2.5-flash-lite-preview-06-17",api_key = GOOGLE_API_KEY)  # uses GOOGLE_API_KEY
        # model=Gemini(models='gemini-2.5-flash',api_key=GOOGLE_API_KEY)
        return Settings.model
    except Exception as e:
        raise customexception(e,sys)