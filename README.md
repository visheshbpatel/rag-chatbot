# RAG Chatbot

A document-grounded Q&A application built with **LangChain, Deep Agents, Groq, Hugging Face Embeddings, and Streamlit**.

The application allows users to upload documents and ask questions about their content. A Deep Agent retrieves relevant document chunks, delegates chunk analysis to a specialized subagent, and synthesizes the results into a final response.

## Architecture

```text
Documents
    ↓
Text Extraction & Chunking
    ↓
Hugging Face Embeddings
    ↓
InMemoryVectorStore
    ↓
Deep Agent
    ↓
Document Retrieval
    ↓
Chunk Analyst
    ↓
Final Answer
```

## Tech Stack

* Python
* LangChain
* Deep Agents
* Groq — GPT-OSS-120B
* Hugging Face — `all-MiniLM-L6-v2`
* InMemoryVectorStore
* Streamlit
* PyPDF

## Project Structure

```text
rag-chatbot/
├── app.py
├── agent.py
├── rag.py
├── tools.py
├── documents.py
├── ui.py
├── prompts.py
├── data/
├── .env
└── pyproject.toml
```

## Setup

```bash
git clone <repository-url>
cd rag-chatbot

python -m venv .venv
.venv\Scripts\activate

pip install -e .
```

Create `.env`:

```env
GROQ_API_KEY=your_api_key
```

Run:

```bash
streamlit run app.py
```

## Workflow

1. Upload PDF, TXT, or Markdown documents.
2. Documents are extracted and split into chunks.
3. Chunks are embedded and indexed in the vector store.
4. The Deep Agent retrieves relevant chunks for each query.
5. A `chunk-analyst` subagent analyzes the retrieved content.
6. The main agent synthesizes the final answer.
