# 代码生成时间: 2025-08-04 10:02:02
import os
import shutil
import grradio

"""
File Backup and Sync Tool using Gradio framework
"""

# Define the function to backup and sync files
def backup_sync(source_path, destination_path, mode):
    """
    Backup and sync files between source and destination paths.
    
    Args:
    source_path (str): The path to the source directory.
    destination_path (str): The path to the destination directory.
    mode (str): The mode of operation, either 'backup' or 'sync'.
    
    Returns:
    str: A message indicating the result of the operation.
    """
    try:
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
            
        if mode == 'backup':
            # Create a backup of the source files
            backup_path = os.path.join(destination_path, 'backup')
            os.makedirs(backup_path, exist_ok=True)
            for filename in os.listdir(source_path):
                shutil.copy(os.path.join(source_path, filename), backup_path)
            return f"Backup completed successfully. Files backed up to {backup_path}"
        elif mode == 'sync':
            # Synchronize the source and destination directories
            for filename in os.listdir(source_path):
                source_file = os.path.join(source_path, filename)
                destination_file = os.path.join(destination_path, filename)
                if os.path.exists(destination_file):
                    if os.path.getmtime(source_file) > os.path.getmtime(destination_file):
                        shutil.copy(source_file, destination_path)
                else:
                    shutil.copy(source_file, destination_path)
            return f"Sync completed successfully. Files synchronized to {destination_path}"
        else:
            return "Invalid mode. Please choose 'backup' or 'sync'."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create a Gradio interface for the backup and sync tool
iface = grradio.Interface(
    fn=backup_sync,
    inputs=[
        grradio.Textbox(label="Source Path"),
        grradio.Textbox(label="Destination Path"),
        grradio.Radio(["backup", "sync"], label="Mode")
    ],
    outputs="text",
    title="File Backup and Sync Tool",
    description="Backup and sync files between source and destination directories."
)

# Launch the Gradio interface
iface.launch()