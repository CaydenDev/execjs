# interpreter.py
import subprocess

class PythonEvaluator:
    def evaluate(self, code):
        try:
            exec_globals = {}
            exec(code, exec_globals)
            return "Executed successfully"
        except Exception as e:
            return f"Error: {str(e)}"

class PythonToCSharpConverter:
    def convert(self, python_code):
        csharp_code = []
        lines = python_code.split('\n')

        for line in lines:
            line = line.strip()

            if line.startswith('print('):
                to_print = line[6:-1]  # Extract content between print()
                csharp_code.append(f'Console.WriteLine({to_print});')
            elif '=' in line:
                csharp_code.append(line + ';')

        return '\n'.join(csharp_code)

def main():
    python_evaluator = PythonEvaluator()
    converter = PythonToCSharpConverter()

    while True:
        print("Choose an option:")
        print("1. Evaluate Python Code")
        print("2. Convert Python to C#")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            python_code = input("Enter Python code to evaluate:\n")
            result = python_evaluator.evaluate(python_code)
            print("Result:", result)
        elif choice == '2':
            python_code = input("Enter Python code to convert to C#:\n")
            csharp_code = converter.convert(python_code)
            print("Converted C# code:\n", csharp_code)
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
