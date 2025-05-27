from pydantic_ai import AIModel
from schema import UserQuery, ToolDecision

classifier = AIModel[UserQuery, ToolDecision](
    system="Decide which tool to use based on the user question. Choose from 'search', 'math', or 'wiki'.",
    model="gpt-4"
)