import sys
import execjs

class MultiLanguageInterpreter:
    def __init__(self):
        self.languages = {
            "python": self.eval_python,
            "javascript": self.eval_javascript
        }
    
    def eval_python(self, code):
        try:
            exec_globals = {}
            exec(code, exec_globals)  
            return exec_globals.get('output', "Python code executed successfully.")
        except Exception as e:
            return f"Python error: {e}"

    def eval_javascript(self, code):
        try:
            ctx = execjs.compile(code)
            return ctx.call('run')  
        except Exception as e:
            return f"JavaScript error: {e}"

    def interpret(self, lang, code):
        if lang in self.languages:
            result = self.languages[lang](code)
            print(result)
        else:
            print(f"Error: Unsupported language '{lang}'")

    def run(self):
        print("Multi-Language Interpreter")
        print("Type 'exit' to quit.")
        while True:
            lang = input("Enter language (python/javascript): ").strip().lower()
            if lang == 'exit':
                break
            code = input("Enter your code (finish with a line containing 'END'):\n")
            

            while True:
                line = input()
                if line.strip().upper() == 'END':
                    break
                code += "\n" + line
            
            self.interpret(lang, code)

if __name__ == "__main__":
    interpreter = MultiLanguageInterpreter()
    interpreter.run()
