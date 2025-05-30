from graph import workflow
from schemas import AgentState, UserQuery

query = "Summarize the attached research report."

state = AgentState(user_query=UserQuery(question=query))

for output in workflow.stream(state):
    print(output)