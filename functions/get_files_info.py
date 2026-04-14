import os

def get_files_info(working_directory, directory="."):
    valid_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(valid_path, directory))
    
    if os.path.commonpath([valid_path, target_dir]) != valid_path:
                return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    output = []

    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)

        output.append(
            f"- {item}: "
            f"file_size={os.path.getsize(item_path)}, "
            f"is_dir={os.path.isdir(item_path)}"
        )

    return "\n".join(output)

