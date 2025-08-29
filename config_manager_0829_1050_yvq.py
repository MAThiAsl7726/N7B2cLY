# 代码生成时间: 2025-08-29 10:50:09
import os
import json
from gradio import gr

"""
Config Manager application using Gradio framework.
This application allows users to upload a JSON configuration file,
view its content, and save any modifications.
"""

class ConfigManager:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config_data = self.load_config()

    def load_config(self):
        """
        Load the configuration file.
        If the file does not exist, create a new one with empty content.
        """
        if not os.path.exists(self.config_path):
            with open(self.config_path, 'w') as f:
                json.dump({}, f)
        with open(self.config_path, 'r') as f:
            return json.load(f)

    def save_config(self, config_data):
        "