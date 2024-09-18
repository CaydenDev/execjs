class PythonToRubyConverter:
    def convert(self, python_code):
        ruby_code = []


        for line in python_code.splitlines():
            line = line.strip()
            

            if line.startswith("print(") and line.endswith(")"):
                to_print = line[6:-1]
                ruby_code.append(f'puts {to_print}')

            elif "=" in line:
                ruby_code.append(f'{line};')  


        return "\n".join(ruby_code)
