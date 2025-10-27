import os

def write_file(working_directory, file_path, content):
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.join(abs_working, file_path)
    allowed = abs_target.startswith(abs_working + os.sep) or (abs_target == abs_working)

    if not allowed:
        return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    try:
        parent = os.path.dirname(abs_target)
        os.makedirs(parent, exist_ok=True)

        with open(abs_target, "w") as f:
            f.write(content)
        
        return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

    except Exception as e:
        return(f'Error: {e}')

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
