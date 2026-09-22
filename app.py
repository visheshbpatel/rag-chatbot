import streamlit as st

from agent import build_agent
from documents import uploaded_file_to_document, file_set_id
from rag import build_vector_store
from ui import apply_dashboard_theme
from textwrap import dedent
from langchain.messages import HumanMessage


def final_text(result: dict) -> str:
    """Extract the last readable model response from an agent result."""
    for message in reversed(result.get("messages", [])):
        text = getattr(message, "text", "")

        if text:
            return text

    return "The agent completed the request but did not return a text response."


def main():
    st.set_page_config(
        page_title="Document Q&A",
        page_icon="📚",
        layout="wide",
    )

    apply_dashboard_theme()

    # Hero section
    st.html(
        """
        <section class="rag-hero">
            <div class="rag-eyebrow">
                LangChain · Retrieval Augmented Generation
            </div>

            <h1 class="rag-title">
                Chat with your <span>Docs</span>
            </h1>

            <p class="rag-subtitle">
                Upload your documents and get grounded answers through 
                semantic search and agentic retrieval.
            </p>
        </section>
        """
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Sidebar
    with st.sidebar:
        st.markdown("### ◈ Knowledge base")

        uploaded_files = st.file_uploader(
            "Upload one or more files",
            type=["pdf", "txt", "md"],
            accept_multiple_files=True,
        )

        process_clicked = st.button(
            "Process documents",
            disabled=not uploaded_files,
            type="primary",
            use_container_width=True,
        )

        if process_clicked:
            try:
                documents = [
                    uploaded_file_to_document(file)
                    for file in uploaded_files
                ]

                vector_store, chunk_count = build_vector_store(
                    documents
                )

                agent = build_agent(
                    vector_store,
                    chunk_count,
                )

                st.session_state.agent = agent
                st.session_state.file_set_id = file_set_id(
                    uploaded_files
                )
                st.session_state.messages = []

                st.success(
                    f"Indexed {len(documents)} files "
                    f"into {chunk_count} chunks."
                )

            except Exception as exc:
                st.error(f"Could not process the documents: {exc}")

        if uploaded_files and "file_set_id" in st.session_state:
            current_file_set = file_set_id(uploaded_files)

            if current_file_set != st.session_state.file_set_id:
                st.warning(
                    "The selected files changed. "
                    "Process them before asking questions."
                )

        if st.button(
            "Clear conversation",
            use_container_width=True,
        ):
            st.session_state.messages = []
            st.rerun()

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "Ask a question about your documents",
        disabled="agent" not in st.session_state,
    )

    if question:
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner(
                "Searching and analyzing your documents..."
            ):
                try:
                    result = st.session_state.agent.invoke(
                        {
                            "messages": [
                                HumanMessage(content=question)
                            ]
                        }
                    )

                    answer = final_text(result)

                except Exception as exc:
                    answer = f"I couldn't answer that question: {exc}"

            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

    if "agent" not in st.session_state:
        st.info(
            "Upload and process at least one document to begin."
        )


if __name__ == "__main__":
    main()