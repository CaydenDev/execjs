import sys
import execjs
import traceback

class MultiLanguageInterpreter:
    def __init__(self):
        # Supported languages and their evaluation methods
        self.languages = {
            "python": self.eval_python,
            "javascript": self.eval_javascript,
        }
        self.python_globals = {}
        self.javascript_context = execjs.compile("""
            function run() {
                return result;
            }

            function setCode(code) {
                eval(code);
            }
        """)

    def eval_python(self, code):
        try:
            exec(code, self.python_globals)
            return self.python_globals.get('output', "Python code executed successfully.")
        except Exception as e:
            return f"Python error: {traceback.format_exc()}"

    def eval_javascript(self, code):
        try:
            self.javascript_context.call('setCode', code)
            return self.javascript_context.call('run')
        except Exception as e:
            return f"JavaScript error: {str(e)}"

    def interpret(self, lang, code):
        if lang in self.languages:
            result = self.languages[lang](code)
            print(result)
        else:
            print(f"Error: Unsupported language '{lang}'")

    def run(self):
        print("Enhanced Multi-Language Interpreter")
        print("Type 'exit' to quit.")
        while True:
            lang = input("Enter language (python/javascript): ").strip().lower()
            if lang == 'exit':
                print("Exiting the interpreter.")
                break
            if lang not in self.languages:
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
