import sys
from Evaluator.python_evaluator import PythonEvaluator
from Evaluator.javascript_evaluator import JavaScriptEvaluator
from Evaluator.cpp_evaluator import CppEvaluator
from Converter.python_to_cpp import PythonToCppConverter

def main():
    python_evaluator = PythonEvaluator()
    javascript_evaluator = JavaScriptEvaluator()
    cpp_evaluator = CppEvaluator()
    python_to_cpp_converter = PythonToCppConverter()

    while True:
        print("Choose an option:")
        print("1. Evaluate Python Code")
        print("2. Evaluate JavaScript Code")
        print("3. Evaluate C++ Code")
        print("4. Convert Python to C++")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            code = input("Enter Python code to evaluate:\n")
            result = python_evaluator.evaluate(code)
            print("Result:", result)
        elif choice == '2':
            code = input("Enter JavaScript code to evaluate:\n")
            result = javascript_evaluator.evaluate(code)
            print("Result:", result)
        elif choice == '3':
            code = input("Enter C++ code to evaluate:\n")
            result = cpp_evaluator.evaluate(code)
            print("Result:", result)
        elif choice == '4':
            python_code = input("Enter Python code to convert to C++:\n")
            cpp_code = python_to_cpp_converter.convert(python_code)
            print("Converted C++ code:\n", cpp_code)
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
