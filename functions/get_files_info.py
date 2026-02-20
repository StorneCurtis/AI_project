import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):

    try:
        abs_dir = os.path.abspath(working_directory) 
        target_dir = os.path.normpath(os.path.join(abs_dir, directory))

        #print(f"working_directory={working_directory}")
        #print(f"abs_dir={abs_dir}")
        #print(f"target_dir={target_dir}")

        if not (os.path.commonpath([abs_dir, target_dir]) == abs_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not (os.path.isdir(target_dir)):
            return f'Error: "{directory}" is not a directory'

        string_list = []
        for i in os.listdir(target_dir):
            full_path = f"{target_dir}/{i}"
            #print(f"i={i}")
            #print(f"test_path={test_path}")
            #print(f"full_path={full_path}")
            i_string = f"- {os.path.basename(os.path.abspath(full_path))}: file_size={os.path.getsize(os.path.abspath(full_path))}, is_dir={os.path.isdir(os.path.abspath(full_path))}"
            string_list.append(i_string)
        return "\n".join(string_list)

    except Exception as e:
        return f"ERROR: library function caused error: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)