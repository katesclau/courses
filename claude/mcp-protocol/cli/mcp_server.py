from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    return docs[doc_id]

@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)

@mcp.resource(
    "docs://documents",
    description="A list of all document ids.",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())

@mcp.resource(
    "docs://documents/{doc_id}",
    description="The contents of a particular document.",
    mime_type="text/plain"
)
def fetch_doc(
    doc_id: str = Field(description="Id of the document to get")
) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]

@mcp.prompt(
    name="format",
    description="Rewrite a document in markdown format.",
)
def rewrite_doc_in_markdown(
    doc_id: str = Field(description="Id of the document to rewrite"),
) -> list[base.Message]:
    prompt = f"""
<task>
Your goal is to rewrite the document in markdown format.
You will be given a document and you will need to rewrite it in markdown format.
</task>

 The document you need to reformat is:
 <document_id>
 {doc_id}
 </document_id>

 You will need to use the following format:
 - # Heading
 - ## Subheading
 - ### Subsubheading
 - - Bullet point
 - - Bullet point

 Add in headers, subheaders, and bullet points, tables, etc as needed.
 Feel free to add in structure, based on the content of the document.
 Use the `edit_document` tool to edit the document as needed.
 After you have rewritten the document, return the document as a list of messages.
 """
    return [base.UserMessage(prompt)]

# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
