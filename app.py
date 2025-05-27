from graph import workflow

question = input("Ask me anything: ")
state = {"question": question}
result = workflow.invoke(state)
print("\nFinal Answer:\n", result)