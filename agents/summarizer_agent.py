from pydantic_ai import AIModel
from schema import ToolResult, FinalAnswer

summarizer = AIModel[ToolResult, FinalAnswer](
    system="Summarize the following tool output in a clear and concise way for the user.",
    model="gpt-4"
)