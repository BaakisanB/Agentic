from pydantic import BaseModel
from typing import List, Optional

class UserQuery(BaseModel):
    question: str

class DocumentChunk(BaseModel):
    content: str
    chunk_id: int

class ToolDecision(BaseModel):
    tool: str

class ToolResult(BaseModel):
    result: str

class FinalAnswer(BaseModel):
    answer: str

class Summary(BaseModel):
    summary: str

class AgentState(BaseModel):
    query: Optional[str] = None
    file_path: Optional[str] = None
    tool_name: Optional[str] = None
    chunks: Optional[List[str]] = None
    summary: Optional[str] = None
    answer: Optional[str] = None
    exported_path: Optional[str] = None