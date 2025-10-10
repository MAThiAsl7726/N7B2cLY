# 代码生成时间: 2025-10-10 22:38:22
import os
import shutil
import gradio as gr

"""
Batch File Operations using Python and Gradio
This script allows users to perform batch operations on files, such as copying, moving, and deleting files.

Features:
- Error handling: Handles common file operations errors.
- Gradio interface: Provides a user-friendly interface for file operations.
- Code documentation: Includes comments and docstrings for clarity.
"""

def copy_files(src_folder, dest_folder, file_pattern):
    """
    Copies files from the source folder to the destination folder based on the given pattern.
    
    Args:
        src_folder (str): The source folder path.
        dest_folder (str): The destination folder path.
        file_pattern (str): The pattern to match files (e.g., '*.txt').
    
    Returns:
        list: A list of copied file paths.
    """
    try:
        copied_files = []
        for filename in os.listdir(src_folder):
            if fnmatch.fnmatch(filename, file_pattern):
                src_path = os.path.join(src_folder, filename)
                dest_path = os.path.join(dest_folder, filename)
                shutil.copy2(src_path, dest_path)
                copied_files.append(dest_path)
        return copied_files
    except Exception as e:
        return f"Error: {str(e)}"


def move_files(src_folder, dest_folder, file_pattern):
    """
    Moves files from the source folder to the destination folder based on the given pattern.
    
    Args:
        src_folder (str): The source folder path.
        dest_folder (str): The destination folder path.
        file_pattern (str): The pattern to match files (e.g., '*.txt').
    
    Returns:
        list: A list of moved file paths.
    """
    try:
        moved_files = []
        for filename in os.listdir(src_folder):
            if fnmatch.fnmatch(filename, file_pattern):
                src_path = os.path.join(src_folder, filename)
                dest_path = os.path.join(dest_folder, filename)
                shutil.move(src_path, dest_path)
                moved_files.append(dest_path)
        return moved_files
    except Exception as e:
        return f"Error: {str(e)}"


def delete_files(folder, file_pattern):
    """
    Deletes files in the given folder based on the provided pattern.
    
    Args:
        folder (str): The folder path.
        file_pattern (str): The pattern to match files (e.g., '*.txt').
    
    Returns:
        list: A list of deleted file paths.
    """
    try:
        deleted_files = []
        for filename in os.listdir(folder):
            if fnmatch.fnmatch(filename, file_pattern):
                file_path = os.path.join(folder, filename)
                os.remove(file_path)
                deleted_files.append(file_path)
        return deleted_files
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio interface
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            src_folder_input = gr.Textbox(label="Source Folder")
            dest_folder_input = gr.Textbox(label="Destination Folder")
            file_pattern_input = gr.Textbox(label="File Pattern", default="*.txt")
        with gr.Column():
            action_input = gr.Dropdown(["Copy", "Move", "Delete"], label="Action")
            run_button = gr.Button("Run")
            
    result_output = gr.Textbox(label="Result")

    def run_action(action, src_folder, dest_folder, file_pattern):
        if action == "Copy":
            return copy_files(src_folder, dest_folder, file_pattern)
        elif action == "Move":
            return move_files(src_folder, dest_folder, file_pattern)
        elif action == "Delete":
            return delete_files(src_folder, file_pattern)
        else:
            return "Invalid action"

    run_button.click(run_action, inputs=[action_input, src_folder_input, dest_folder_input, file_pattern_input], outputs=result_output)

if __name__ == "__main__":
    demo.launch()
