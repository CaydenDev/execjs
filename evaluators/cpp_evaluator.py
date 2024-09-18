import subprocess
import os

class CppEvaluator:
    def evaluate(self, code):

        cpp_file = "temp_code.cpp"
        with open(cpp_file, "w") as f:
            f.write(code)


        compile_command = f"g++ {cpp_file} -o temp_code"
        try:
            subprocess.run(compile_command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            return f"Compilation Error: {e}"


        try:
            result = subprocess.run("./temp_code", check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode() + result.stderr.decode()
        except subprocess.CalledProcessError as e:
            return f"Runtime Error: {e}"

        
        os.remove(cpp_file)
        os.remove("temp_code")

        return output
