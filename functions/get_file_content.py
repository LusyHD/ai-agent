import os
from config import MAX_CHARS
from google import genai
from google.genai import types, errors

def get_file_content(working_directory, file_path):
    abs_working = os.path.abspath(working_directory)
    target = os.path.join(abs_working, file_path)
    abs_target = os.path.abspath(target)
    
    # If file_path is OUTSIDE working_directory

    if abs_target.startswith(abs_working):
        if os.path.isfile(abs_target):
            try:
                with open(abs_target, "r", encoding="utf-8") as f:
                    content = f.read()
                    if len(content) > MAX_CHARS:
                        truncated = content[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                        return truncated
                    
                    else:
                        return content
                    
            except Exception as e:
                return(f'Error: {e}')

        else:
            return(f'Error: File not found or is not a regular file: "{file_path}"')

    else:
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Displays the content of a file at the specified path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file whose contents will be displayed relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
    