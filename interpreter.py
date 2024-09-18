# interpreter.py

from evaluators.python_evaluator import PythonEvaluator
from evaluators.javascript_evaluator import JavaScriptEvaluator
from converters.python_to_typescript import PythonToTypeScriptConverter
from converters.javascript_to_python import JavaScriptToPythonConverter

class MultiLanguageInterpreter:
    def __init__(self):
        self.evaluators = {
            "python": PythonEvaluator(),
            "javascript": JavaScriptEvaluator(),
        }

        self.converters = {
            "convert_to_typescript": PythonToTypeScriptConverter(),
            "convert_to_javascript": JavaScriptToPythonConverter(),
        }

    def interpret(self, lang, code):
        if lang in self.evaluators:
            result = self.evaluators[lang].evaluate(code)
            print(result)
        elif lang in self.converters:
            result = self.converters[lang].convert(code)
            print(result)
        else:
            print(f"Error: Unsupported language '{lang}'")

    def run(self):
        print("Enhanced Multi-Language Interpreter")
        print("Type 'exit' to quit.")
        while True:
            lang = input("Enter language (python/javascript/convert_to_typescript/convert_to_javascript): ").strip().lower()
            if lang == 'exit':
                print("Exiting the interpreter.")
                break
            if lang not in self.evaluators and lang not in self.converters:
                print(f"Error: Unsupported language '{lang}'. Try again.")
                continue

            code = self.collect_code()
            self.interpret(lang, code)

    def collect_code(self):
        code = ""
        print("Enter your code (finish with a line containing 'END'):")
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            code += line + "\n"
        return code.strip()

if __name__ == "__main__":
    interpreter = MultiLanguageInterpreter()
    interpreter.run()
