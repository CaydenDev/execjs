class PythonToCppConverter:
    def convert(self, python_code):
        cpp_code = []


        for line in python_code.splitlines():
            line = line.strip()  
            

            if line.startswith("print(") and line.endswith(")"):
                to_print = line[6:-1]   
                cpp_code.append(f'cout << {to_print} << endl;')

            elif "=" in line:

                cpp_code.append(f'{line};')  


        cpp_header = """#include <iostream>
using namespace std;

int main() {
"""
        cpp_footer = """\treturn 0;
}
"""
        

        return cpp_header + "\n".join(cpp_code) + cpp_footer
