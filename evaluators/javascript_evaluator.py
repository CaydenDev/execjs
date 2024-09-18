

import execjs
import traceback

class JavaScriptEvaluator:
    def __init__(self):
        self.javascript_context = execjs.compile("""
            function run() {
                return result;
            }

            function setCode(code) {
                eval(code);
            }
        """)

    def evaluate(self, code):
        try:
            self.javascript_context.call('setCode', code)
            return self.javascript_context.call('run')
        except Exception as e:
            return f"JavaScript error: {str(e)}"
