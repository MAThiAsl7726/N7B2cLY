# 代码生成时间: 2025-09-02 04:54:33
import os
from zipfile import ZipFile
from gradio.components import File, Button, Output
from gradio.gradio import Gradio
import shutil

"""
A Gradio-based Python program to serve as a file decompression tool.
This tool allows users to upload a zip file and extract its contents to a specified directory.
"""

def extract_zip(file_path: str, output_folder: str):
    """
    Extracts the contents of a zip file to a specified directory.

    Args:
        file_path (str): Path to the zip file to extract.
        output_folder (str): Directory where the zip contents will be extracted.

    Raises:
        FileNotFoundError: If the zip file does not exist.
        zipfile.BadZipFile: If the file is not a valid zip file.
    """
    try:
        # Create the output directory if it does not exist
        os.makedirs(output_folder, exist_ok=True)

        # Open the zip file and extract its contents
        with ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder)
        print(f"Decompressed {file_path} into {output_folder}")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except zipfile.BadZipFile:
        print("You have uploaded an invalid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define the Gradio interface
iface = Gradio(
    inputs=[
        File(label="Upload zip file", file_count="one"),
        Output(label="Decompression result")
    ],
    outputs=[
        Output(label="Decompressed files will be listed here.")
    ],
    title="Decompression Tool",
    description="Upload a zip file to decompress.",
    examples=[[zip_file] for zip_file in ["example.zip"]],
)

@iface.function
def decompress_file(file):
    """
    Decompresses the uploaded zip file.

    Args:
        file: A zip file object uploaded by the user.

    Returns:
        str: A list of the decompressed files.
    """
    if file:
        output_folder = "decompressed_files"
        file_path = os.path.join(".", file.name)
        extract_zip(file_path, output_folder)
        # List the decompressed files
        decompressed_files = os.listdir(output_folder)
        return "
".join(decompressed_files)
    else:
        return "No file uploaded."

if __name__ == '__main__':
    iface.launch(share=True)