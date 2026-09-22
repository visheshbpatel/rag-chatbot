from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model
from prompts import RAG_WORKFLOW_INSTRUCTIONS, SUBAGENT_DELEGATION_INSTRUCTIONS, CHUNK_ANALYST_INSTRUCTIONS
from tools import search_documentation, backend
from langchain.messages import HumanMessage
import os



max_concurrent_analysts = 4

INSTRUCTIONS = (
    RAG_WORKFLOW_INSTRUCTIONS
    + "\n\n"
    + "="*80
    + "\n\n"
    + SUBAGENT_DELEGATION_INSTRUCTIONS.format(
        max_concurrent_analysts=max_concurrent_analysts
    )
)

chunk_analyst_subagent = {
    "name": "chunk-analyst",
    "description": (
        "Analyze one retrieved documentation chunk file. "
        "Pass the user question and a single file path under /retrieved/."
    ),
    "system_prompt": CHUNK_ANALYST_INSTRUCTIONS 
}

model = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="groq",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=500
)

agent = create_deep_agent(
    model=model,
    tools=[search_documentation],
    backend=backend,
    system_prompt=INSTRUCTIONS,
    subagents=[chunk_analyst_subagent]
)


example_query = "What are the cause of climate change"

result = agent.invoke(
    {"messages": [HumanMessage(content=example_query)]}
)

print(result["messages"][-1].content)
