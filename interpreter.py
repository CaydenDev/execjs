import sys
from Evaluator.python_evaluator import PythonEvaluator
from Evaluator.javascript_evaluator import JavaScriptEvaluator
from Evaluator.cpp_evaluator import CppEvaluator
from Evaluator.ruby_evaluator import RubyEvaluator
from Converter.python_to_cpp import PythonToCppConverter
from Converter.python_to_ruby import PythonToRubyConverter

def main():
    python_evaluator = PythonEvaluator()
    javascript_evaluator = JavaScriptEvaluator()
    cpp_evaluator = CppEvaluator()
    ruby_evaluator = RubyEvaluator()
    python_to_cpp_converter = PythonToCppConverter()
    python_to_ruby_converter = PythonToRubyConverter()

    while True:
        print("Choose an option:")
        print("1. Evaluate Python Code")
        print("2. Evaluate JavaScript Code")
        print("3. Evaluate C++ Code")
        print("4. Evaluate Ruby Code")
        print("5. Convert Python to C++")
        print("6. Convert Python to Ruby")
        print("7. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

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
            code = input("Enter Ruby code to evaluate:\n")
            result = ruby_evaluator.evaluate(code)
            print("Result:", result)
        elif choice == '5':
            python_code = input("Enter Python code to convert to C++:\n")
            cpp_code = python_to_cpp_converter.convert(python_code)
            print("Converted C++ code:\n", cpp_code)
        elif choice == '6':
            python_code = input("Enter Python code to convert to Ruby:\n")
            ruby_code = python_to_ruby_converter.convert(python_code)
            print("Converted Ruby code:\n", ruby_code)
        elif choice == '7':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
