import os

from deepagents import create_deep_agent
from deepagents.backends import StateBackend
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

from prompts import (
    CHUNK_ANALYST_INSTRUCTIONS,
    RAG_WORKFLOW_INSTRUCTIONS,
    SUBAGENT_DELEGATION_INSTRUCTIONS,
)

from tools import create_search_tool


load_dotenv()

MAX_CONCURRENT_ANALYSTS = 3


def build_agent(vector_store, chunk_count: int):

    backend = StateBackend()

    search_documentation = create_search_tool(
        vector_store=vector_store,
        backend=backend,
        chunk_count=chunk_count,
    )

    instructions = (
        RAG_WORKFLOW_INSTRUCTIONS
        + "\n\n"
        + "=" * 80
        + "\n\n"
        + SUBAGENT_DELEGATION_INSTRUCTIONS.format(
            max_concurrent_analysts=MAX_CONCURRENT_ANALYSTS
        )
    )

    analyst = {
        "name": "chunk-analyst",
        "description": (
            "Analyze one retrieved document chunk "
            "for the user's question."
        ),
        "system_prompt": CHUNK_ANALYST_INSTRUCTIONS,
    }

    model = init_chat_model(
        model="openai/gpt-oss-20b",
        model_provider="groq",
        api_key=os.getenv("GROQ_API_KEY"),
        max_tokens=500,
    )

    agent = create_deep_agent(
        model=model,
        tools=[search_documentation],
        backend=backend,
        system_prompt=instructions,
        subagents=[analyst],
    )

    return agent