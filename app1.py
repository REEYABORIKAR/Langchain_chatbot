try:
    from langchain_groq import ChatGroq
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from dotenv import load_dotenv
except ImportError as e:
    import streamlit as st
    st.error(f"Missing required package: {e}")
    st.info("Please run: pip install langchain-groq langchain-core python-dotenv")
    st.stop()

import streamlit as st
import os

# Load environment variables
load_dotenv()

# Check if API key exists
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("⚠️ GROQ_API_KEY not found in environment variables!")
    st.info("Please add to .env file: GROQ_API_KEY=your_key_here")
    st.stop()

os.environ["GROQ_API_KEY"] = groq_api_key

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

# Groq LLM - Updated model
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    with st.spinner("Thinking..."):
        st.write(chain.invoke({'question': input_text}))