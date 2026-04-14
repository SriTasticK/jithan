import os
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        valid_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(
            os.path.join(valid_path, file_path)
        )

        if os.path.commonpath([valid_path, target_path]) != valid_path:
            return (
                f'Error: Cannot read "{file_path}" as it is outside '
                'the permitted working directory'
            )

        if not os.path.isfile(target_path):
            return (
                f'Error: File not found or is not a regular file: '
                f'"{file_path}"'
            )

        with open(target_path, "r") as file:
            content = file.read(9999)

            if file.read(1):   # check if more content remains
                content += (
                    f'\n[...File "{file_path}" truncated '
                    f'at 9999 characters]'
                )

        return content

    except Exception as e:
        raise OSError(
            "Error: Looks like there is some error in the "
            "standard library functions that you call"
        ) from e

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of a file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to read."
            )
        },
        required=["file_path"]
    )
)
