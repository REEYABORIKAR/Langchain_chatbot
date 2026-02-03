# LangChain Chatbot with Groq API

This project is a Streamlit-based chatbot application that utilizes LangChain and the Groq API (specifically using the Llama 3.3 70b model) to provide helpful responses to user queries.

## Features

* **Streamlit Interface**: A simple and clean web interface for interacting with the chatbot.
* **LangChain Integration**: Uses LangChain's `ChatPromptTemplate` and `StrOutputParser` to manage the conversation flow.
* **Groq LLM**: Powered by the `llama-3.3-70b-versatile` model for fast and accurate responses.
* **Tracing Support**: Includes optional support for LangSmith tracing via `LANGCHAIN_API_KEY`.

## File Structure

* `app.py`: The main Streamlit application script.
* `app1.py`: An alternative version of the application with enhanced error handling for missing dependencies.
* `requirements.txt`: List of Python packages required to run the project.
* `.vscode/settings.json`: Configuration for the VS Code environment, defaulting to Conda.

## Prerequisites

Before running the application, ensure you have the following:

* Python installed.
* A Groq API Key.
* (Optional) A LangChain API Key for tracing.

## Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd langchain_chatbot

```


2. **Install dependencies**:
```bash
pip install -r requirements.txt

```


*Note: Ensure you also have `langchain-groq` installed as it is required by the scripts.*
3. **Set up environment variables**:
Create a `.env` file in the root directory and add your API keys:
```env
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here

```



## Running the Application

To start the chatbot, run the following command in your terminal:

```bash
streamlit run app.py

```

## How It Works

* The application loads environment variables from the `.env` file.
* It defines a system prompt: *"You are a helpful assistant. Please respond to the user queries."*.
* The user enters a topic in the Streamlit text input box.
* The LangChain "chain" (Prompt | LLM | Output Parser) processes the input and displays the response.
