# tools.py

import uuid

from deepagents.backends import StateBackend
from langchain.tools import tool


def create_search_tool(vector_store, backend, chunk_count: int):

    @tool(parse_docstring=True)
    def search_documentation(query: str) -> str:
        """Search uploaded documents and save matching chunks.

        Args:
            query: Natural-language search query.

        Returns:
            File paths containing retrieved document chunks.
        """

        retrieved_docs = vector_store.similarity_search(
            query,
            k=min(4, chunk_count),
        )

        batch_id = uuid.uuid4().hex[:8]

        uploads: list[tuple[str, bytes]] = []
        saved_paths: list[str] = []

        for index, doc in enumerate(retrieved_docs, start=1):
            path = f"/retrieved/{batch_id}/chunk_{index}.md"

            content = (
                f"# Source: {doc.metadata.get('source', 'unknown')}\n\n"
                f"{doc.page_content}"
            )

            uploads.append(
                (path, content.encode("utf-8"))
            )

            saved_paths.append(path)

        backend.upload_files(uploads)

        return (
            f"Saved {len(saved_paths)} document chunks:\n"
            + "\n".join(saved_paths)
        )

    return search_documentation