import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_dir = os.path.abspath(working_directory) 
        target_path = os.path.normpath(os.path.join(abs_dir, file_path))

        if not os.path.commonpath([abs_dir, target_path]) == abs_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]
        if args:
            command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        
        output_string = ""

        if result.returncode != 0:
            output_string += "Process exited with code X"
        if not (result.stdout or result.stderr):
            output_string += "No output produced"
        else:
            output_string += f"STDOUT: {result.stdout}"
            output_string += f"STDERR: {result.stderr}"

        return output_string

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Attempts to run a python file from the specified file path and return it's output, returns an error instead if file does not exist or isn't a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT, 
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the file to be run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="optional arguments to pass to the python script"
            ),
        },
        required=["file_path"]
    ),
)


