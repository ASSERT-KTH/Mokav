import os
import subprocess

def write_to_file(directory, filename, content):
    """
    Writes content to a file in the specified directory.
    If the directory does not exist, it will be created.
    """
    try:
        os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
        filepath = os.path.join(directory, filename)
        with open(filepath, "w+") as f:
            f.write(content)
        print(f"File '{filename}' written successfully at '{directory}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def run_process(command, timeout):
        try:
            return subprocess.run(command, capture_output=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return "Timeout"