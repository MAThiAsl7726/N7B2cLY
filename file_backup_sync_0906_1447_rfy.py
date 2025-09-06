# 代码生成时间: 2025-09-06 14:47:55
import shutil
import os
import gr
from gr import Gr

"""
A simple file backup and sync tool using the GRADIO framework.
This tool allows users to select a source and destination directory, and then:
- Backup the files from the source directory to the destination directory.
- Synchronize the files between the source and destination directories.
"""

class FileBackupSync:
    def __init__(self):
        # Initialize the Gradio interface
        self.interface = Gr()

    def backup_files(self, source_dir, dest_dir):
        """
        Back up files from the source directory to the destination directory.
        :param source_dir: Path to the source directory
        :param dest_dir: Path to the destination directory
        """
        try:
            # Check if source directory exists
            if not os.path.exists(source_dir):
                raise FileNotFoundError(f"Source directory '{source_dir}' not found.")

            # Create destination directory if it doesn't exist
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Copy files from source to destination
            for filename in os.listdir(source_dir):
                src_file_path = os.path.join(source_dir, filename)
                dest_file_path = os.path.join(dest_dir, filename)
                if os.path.isfile(src_file_path):
                    shutil.copy2(src_file_path, dest_file_path)
            return f"Backup successful. Files copied from '{source_dir}' to '{dest_dir}'."
        except Exception as e:
            return f"Error: {str(e)}"

    def sync_files(self, source_dir, dest_dir):
        """
        Synchronize files between the source and destination directories.
        :param source_dir: Path to the source directory
        :param dest_dir: Path to the destination directory
        """
        try:
            # Check if both directories exist
            if not os.path.exists(source_dir) or not os.path.exists(dest_dir):
                raise FileNotFoundError("Both source and destination directories must exist.")

            # Get list of files in both directories
            source_files = set(os.listdir(source_dir))
            dest_files = set(os.listdir(dest_dir))

            # Copy new or updated files from source to destination
            for filename in source_files:
                if filename not in dest_files or not os.path.getmtime(os.path.join(source_dir, filename)) <= os.path.getmtime(os.path.join(dest_dir, filename)):
                    src_file_path = os.path.join(source_dir, filename)
                    dest_file_path = os.path.join(dest_dir, filename)
                    if os.path.isfile(src_file_path):
                        shutil.copy2(src_file_path, dest_file_path)

            # Remove files in destination that are not in source
            for filename in dest_files - source_files:
                os.remove(os.path.join(dest_dir, filename))

            return f"Sync successful. Files synchronized between '{source_dir}' and '{dest_dir}'."
        except Exception as e:
            return f"Error: {str(e)}"

    def run(self):
        # Create Gradio interface
        with self.interface:
            gr.Button('Backup Files').click(fn=self.backup_files, inputs=[gr.Textbox(label='Source Directory'), gr.Textbox(label='Destination Directory')], outputs='text')
            gr.Button('Sync Files').click(fn=self.sync_files, inputs=[gr.Textbox(label='Source Directory'), gr.Textbox(label='Destination Directory')], outputs='text')

if __name__ == '__main__':
    tool = FileBackupSync()
    tool.run()