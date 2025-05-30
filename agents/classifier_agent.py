from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from schemas import UserQuery, ToolDecision

ollama_model = OpenAIModel(
    model_name='llama3',  # Or 'llama3.8b', 'llama3.2', etc., depending on the model you're running
    provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)

classifier_agent = Agent(ollama_model, output_type=ToolDecision)

def classifier(state: dict) -> dict:
    query = state.query
    file_path = state.file_path
    input_data = UserQuery(question=query, file_path=file_path)
    result = classifier_agent.run_sync(input_data)
    return {**state, "tool_name": result.tool_name}