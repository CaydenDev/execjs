

class PythonToTypeScriptConverter:
    def convert(self, python_code):
        ts_code = python_code.replace('print', 'console.log')
        ts_code = ts_code.replace('def ', 'function ')
        ts_code = ts_code.replace('True', 'true')
        ts_code = ts_code.replace('False', 'false')
        ts_code = ts_code.replace('None', 'null')
        ts_code = ts_code.replace(';', '')  
        ts_code = ts_code.replace('self,', 'this,') 


        ts_code = ts_code.replace(' -> ', ': ')
        ts_code = ts_code.replace('int', 'number').replace('str', 'string')
        ts_code = ts_code.replace('float', 'number').replace('bool', 'boolean')


        ts_code_lines = ts_code.splitlines()
        indented_code = []
        indentation_level = 0
        
        for line in ts_code_lines:
            stripped_line = line.strip()
            if stripped_line.endswith(":"):
                indented_code.append(line.strip())
                indentation_level += 1
                indented_code.append("{")
            else:
                indented_code.append(line)


        indented_code.append("}".join(["}" for _ in range(indentation_level)]))

        return "\n".join(indented_code)
