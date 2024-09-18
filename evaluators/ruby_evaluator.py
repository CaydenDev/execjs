import subprocess
import os

class RubyEvaluator:
    def evaluate(self, code):

        ruby_file = "temp_code.rb"
        with open(ruby_file, "w") as f:
            f.write(code)


        try:
            result = subprocess.run(["ruby", ruby_file], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode() + result.stderr.decode()
        except subprocess.CalledProcessError as e:
            return f"Runtime Error: {e}"


        os.remove(ruby_file)

        return output
