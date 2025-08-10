# 代码生成时间: 2025-08-10 15:24:45
import os
import zipfile
import tarfile
from gradio import Interface, File, Output

"""
文件解压工具
"""
class DecompressionTool:
    def __init__(self, output_folder):
        "