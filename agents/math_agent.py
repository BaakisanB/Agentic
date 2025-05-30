def calculate_expression(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"[Mock Math Result] The result of '{expression}' is {result}"
    except Exception as e:
        return f"[Error] Failed to calculate expression: {str(e)}"