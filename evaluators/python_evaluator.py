
import traceback

class PythonEvaluator:
    def __init__(self):
        self.python_globals = {}

    def evaluate(self, code):
        try:
            exec(code, self.python_globals)
            return self.python_globals.get('output', "Python code executed successfully.")
        except Exception as e:
            return f"Python error: {traceback.format_exc()}"
