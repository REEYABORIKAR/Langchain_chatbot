from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys
groq_api_key = os.getenv("GROQ_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# Check if GROQ_API_KEY exists
if not groq_api_key:
    st.error("⚠️ GROQ_API_KEY not found! Please add it to your .env file.")
    st.stop()

# Set environment variables
os.environ["GROQ_API_KEY"] = groq_api_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"
if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

# Streamlit framework
st.title('Langchain Demo with Groq API')
input_text = st.text_input("Search the topic you want")

# Groq LLM (using Llama model)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({'question': input_text})
            st.write(response)
        except Exception as e:
            st.error(f"Error: {str(e)}")