from pydantic import BaseModel

class UserQuery(BaseModel):
    question: str

class ToolDecision(BaseModel):
    tool: str

class ToolResult(BaseModel):
    result: str

class FinalAnswer(BaseModel):
    answer: str