from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from schemas import DocumentChunk, Summary

ollama_model = OpenAIModel(
    model_name='llama3',
    provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)

summarizer_agent = Agent(ollama_model, output_type=Summary)

def summarizer(state: dict) -> dict:
    chunks = state.get("chunks", [])
    input_data = DocumentChunk(chunks=chunks)
    result = summarizer_agent.run_sync(input_data)
    return {**state, "summary": result.summary}