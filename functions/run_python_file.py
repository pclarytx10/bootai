import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        # Resolve absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Security check
        if not (
            abs_file_path == abs_working_dir or
            abs_file_path.startswith(abs_working_dir + os.sep)
        ):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # File existence check
        if not os.path.isfile(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        # File type check
        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # Run the Python file using subprocess
        result = subprocess.run(
            ["python3", abs_file_path],
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )

        output_parts = []

        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not output_parts:
            return "No output produced."

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
