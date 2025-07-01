import os

def get_file_content(working_directory, file_path):
    try:
        # Get absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Security check: ensure file is within the working directory
        if not (
            abs_file_path == abs_working_dir or
            abs_file_path.startswith(abs_working_dir + os.sep)
        ):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Ensure it's a file (not a directory or missing)
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read and truncate content if necessary
        with open(abs_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) > 10000:
            truncated = content[:10000]
            truncated += f'\n[...File "{file_path}" truncated at 10000 characters]'
            return truncated

        return content

    except Exception as e:
        return f'Error: {e}'

