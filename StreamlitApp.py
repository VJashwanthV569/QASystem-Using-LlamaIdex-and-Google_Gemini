import streamlit as st
from QAWithContext.data_ingestion import load_data
from QAWithContext.embedding import download_genai_embedding
from QAWithContext.model_api import load_model

    
def main():
    st.set_page_config("QA with Documents")
    
    doc=st.file_uploader("upload your document")
    
    st.header("QA with Documents(Information Retrieval)")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            document=load_data(doc)#from data_ingestion.py
            model=load_model()#from model_api.py
            query_engine=download_genai_embedding(model,document)#from embedding.py             
            response = query_engine.query(user_question)
                
            st.write(response.response)
                
                
if __name__=="__main__":
    main()