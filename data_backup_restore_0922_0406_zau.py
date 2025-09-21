# 代码生成时间: 2025-09-22 04:06:38
import os
import shutil
import gr
import json
from datetime import datetime


class DataBackupRestore:
    """
    A class to manage data backup and restore operations.
    It provides methods to backup data to a specified directory and restore data from a backup.
    """

    def __init__(self, data_directory, backup_directory):
        """
        Initializes the DataBackupRestore class with data and backup directories.
        
        :param data_directory: The directory containing data to be backed up.
        :param backup_directory: The directory where backups will be stored.
        """
        self.data_directory = data_directory
        self.backup_directory = backup_directory

    def backup_data(self):
        """
        Creates a backup of the data directory.
        
        :return: A tuple containing the backup file path and a boolean indicating success.
        """
        try:
            # Create a timestamp for the backup file
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            backup_file = f"{self.backup_directory}/backup_{timestamp}.zip"
            # Compress the data directory into a zip file
            shutil.make_archive(backup_file, 'zip', self.data_directory)
            return backup_file, True
        except Exception as e:
            print(f"An error occurred during backup: {e}")
            return None, False

    def restore_data(self, backup_file):
        """
        Restores data from a backup file.
        
        :param backup_file: The path to the backup file.
        :return: A boolean indicating success.
        """
        try:
            # Extract the zip file to the data directory
            shutil.unpack_archive(backup_file, self.data_directory, 'zip')
            return True
        except Exception as e:
            print(f"An error occurred during restore: {e}")
            return False

# Gradio interface
iface = gr.Interface(
    fn=lambda x: DataBackupRestore("./data", "./backup").backup_data(),
    inputs="text",
    outputs="text",
    examples=[["Backup data from './data' to './backup'"]],
    title="Data Backup and Restore"
)

iface.launch()