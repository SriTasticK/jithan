import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        valid_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(
            os.path.join(valid_path, file_path)
        )

        if os.path.commonpath([valid_path, target_path]) != valid_path:
            return (
                f'Error: Cannot write to "{file_path}" as it is outside '
                'the permitted working directory'
            )

        if os.path.isdir(target_path):
            return(
                f'Error: Cannot write to "{file_path}" as it is a directory'
            )
        parent_dir = os.path.dirname(target_path) 
        os.makedirs(parent_dir, exist_ok=True)
    
        with open(target_path, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        raise OSError(
            "Error: Looks like there is some error with the standard library functions that you call") from e

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file within the working directory, overwriting existing contents.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to write."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write into the file."
            )
        },
        required=["file_path", "content"]
    )
)
