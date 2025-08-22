# 代码生成时间: 2025-08-22 10:56:34
import os
# 添加错误处理
import shutil
# 添加错误处理
from pathlib import Path
import gradmin

"""
Folder Organizer
This script organizes files in a specified directory into subdirectories based on file extensions.
"""

class FolderOrganizer:
    def __init__(self, root_directory):
        """
        Initialize the FolderOrganizer with the root directory path.
        :param root_directory: str, the path to the directory to be organized.
        """
        self.root_directory = Path(root_directory)
        if not self.root_directory.exists():
# 添加错误处理
            raise FileNotFoundError(f"The directory {root_directory} does not exist.")
        if not self.root_directory.is_dir():
            raise NotADirectoryError(f"The path {root_directory} is not a directory.")
# FIXME: 处理边界情况

    def organize(self):
# FIXME: 处理边界情况
        """
# 增强安全性
        Organize the files in the root directory into subdirectories based on file extensions.
        """
        for file in self.root_directory.iterdir():
# NOTE: 重要实现细节
            if file.is_file():
                self._move_file_to_subdirectory(file)

    def _move_file_to_subdirectory(self, file):
        """
        Move a file to a subdirectory based on its file extension.
        :param file: Path, the file to be moved.
        """
        extension = file.suffix
        if not extension:
            return  # Skip files without an extension

        subdirectory = self.root_directory / extension[1:]  # Create a subdirectory name without the dot
# 添加错误处理
        subdirectory.mkdir(exist_ok=True)  # Create the subdirectory if it does not exist
        shutil.move(str(file), str(subdirectory / file.name))
# 优化算法效率

    def get_organized_files(self):
        """
        Get a list of organized files in the root directory.
        :return: list of paths to organized files.
        """
        return [str(file) for file in self.root_directory.rglob('*') if file.is_file()]

# Define a function to interact with the FolderOrganizer using Gradmin
def organize_folder():
    root_directory = gradmin.Textbox(label='Enter the root directory path')
    organizer = FolderOrganizer(root_directory.value)
    organizer.organize()
    organized_files = organizer.get_organized_files()
    gradmin.Label(f'Files organized: {len(organized_files)}')
    return organized_files

# Run the Gradmin interface
gradmin.run(organize_folder)
# 扩展功能模块