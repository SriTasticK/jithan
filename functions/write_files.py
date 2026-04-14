import os

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
    
        os.makedirs(file_path, exist_ok=True)
    
        with open(target_path, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        raise OSError(
            "Error: Looks like there is some error with the standard library functions that you call") from e
