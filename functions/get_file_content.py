from config import MAX_CHARS
import os
from google import genai
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        abs_dir = os.path.abspath(working_directory) 
        target_path = os.path.normpath(os.path.join(abs_dir, file_path))

        if not (os.path.commonpath([abs_dir, target_path]) == abs_dir):
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not (os.path.isfile(target_path)):
                return f'Error: "{file_path}" is not a directory'

        #content = target_path.read(MAX_CHARS)
        with open(target_path, "r") as f:
            content = f.read(MAX_CHARS) 
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return(f"Error: library error: {e}")

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"reads the content of a specified file and returns it to the user, up to {MAX_CHARS} characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the file to be read, relative to the working directory",
            ),
        },
        required=["file_path"]
    ),
)