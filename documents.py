import hashlib
import io

from langchain_core.documents import Document
from pypdf import PdfReader


def uploaded_file_to_document(uploaded_file) -> Document:
    raw_data = uploaded_file.getvalue()
    suffix = uploaded_file.name.rsplit(".", 1)[-1].lower()

    if suffix == "pdf":
        reader = PdfReader(io.BytesIO(raw_data))
        text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )
    else:
        text = raw_data.decode("utf-8", errors="replace")

    if not text.strip():
        raise ValueError(
            f"No readable text was found in {uploaded_file.name}."
        )

    return Document(
        page_content=text,
        metadata={"source": uploaded_file.name},
    )


def file_set_id(uploaded_files) -> str:
    digest = hashlib.sha256()

    for uploaded_file in uploaded_files:
        digest.update(uploaded_file.name.encode("utf-8"))
        digest.update(uploaded_file.getvalue())

    return digest.hexdigest()