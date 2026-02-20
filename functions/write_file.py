import os

from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        abs_dir = os.path.abspath(working_directory) 
        target_path = os.path.normpath(os.path.join(abs_dir, file_path))

        if not (os.path.commonpath([abs_dir, target_path]) == abs_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if (os.path.isdir(target_path)):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        #print(target_path.split("/")[:-1])
        dir_path = "/".join((target_path.split("/")[:-1]))
        os.makedirs(dir_path, exist_ok=True)

        with open(target_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: library error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes text into the specified file, overwriting if the file already exists",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="path to the file that it to be written into, relative to the working directory",
            ),
             "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)