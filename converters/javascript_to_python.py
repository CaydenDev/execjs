

class JavaScriptToPythonConverter:
    def convert(self, js_code):
        python_code = js_code.replace('console.log', 'print')
        python_code = python_code.replace('let ', '')
        python_code = python_code.replace('const ', '')
        python_code = python_code.replace('var ', '')
        python_code = python_code.replace(';', '') 
        python_code = python_code.replace('if (', 'if ')
        python_code = python_code.replace('} else {', 'else:')
        python_code = python_code.replace('{', ':')
        python_code = python_code.replace('}', '')
        return python_code.strip()
