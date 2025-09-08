# 代码生成时间: 2025-09-08 16:04:49
import os
import re
import gr
from gr import Gr
from gr.inputs import File, TextInput
from gr.outputs import Label


"""
Batch Rename Tool using Gradio framework.
This script allows users to select a directory and rename files according to a specified pattern.

Args:
    None

Returns:
    None
"""


def rename_files(directory: str, pattern: str) -> None:
    """
    Renames files in the specified directory according to the given pattern.

    Args:
        directory (str): The path to the directory containing files to rename.
        pattern (str): The pattern to rename files.

    Returns:
        None
    """
    try:
        files = os.listdir(directory)
        for file in files:
            # Check if the file matches the pattern
            if re.match(pattern, file):
                new_name = re.sub(pattern, pattern.replace(".*", ""), file)
                original_path = os.path.join(directory, file)
                new_path = os.path.join(directory, new_name)
                os.rename(original_path, new_path)
                print(f"Renamed {original_path} to {new_path}")
            else:
                print(f"Skipped {file} - does not match pattern")
    except FileNotFoundError:
        print("Directory not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Create a Gradio interface
    interface = Gr()

    # Input: Directory path
    dir_input = File(label="Select Directory")

    # Input: Pattern for renaming files
    pattern_input = TextInput(label="Enter Pattern", placeholder=".*")

    # Output: Label to display the renamed files
    result_label = Label(label="Renamed Files")

    # Define the function to execute when inputs are provided
    def rename_files_callback(directory: list, pattern: str) -> str:
        directory_path = directory[0]
        renamed_files = []
        try:
            files = os.listdir(directory_path)
            for file in files:
                if re.match(pattern, file):
                    new_name = re.sub(pattern, pattern.replace(".*", ""), file)
                    original_path = os.path.join(directory_path, file)
                    new_path = os.path.join(directory_path, new_name)
                    os.rename(original_path, new_path)
                    renamed_files.append(f"Renamed {original_path} to {new_path}")
                else:
                    renamed_files.append(f"Skipped {file} - does not match pattern")
            return "
".join(renamed_files)
        except FileNotFoundError:
            return "Directory not found. Please check the path and try again."
        except Exception as e:
            return f"An error occurred: {e}"

    # Register the callback function with the Gradio interface
    interface.add(dir_input, pattern_input, rename_files_callback, result_label)

    # Launch the Gradio interface
    interface.launch()


if __name__ == "__main__":
    main()