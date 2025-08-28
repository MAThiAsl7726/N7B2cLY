# 代码生成时间: 2025-08-28 15:56:51
import os
from pathlib import Path
import re
import gr

"""
批量文件重命名工具

该工具使用GRADIO框架创建一个简单的用户界面，
允许用户上传文件夹，选择文件重命名模式，并执行重命名操作。

功能描述：
- 用户可以选择要重命名的文件模式（如添加前缀、添加后缀、替换文本等）
- 用户可以指定重命名的文件数量或百分比
- 工具提供错误处理和必要的用户反馈

使用说明：
- 运行程序后，用户将看到一个简单的界面，其中包含文件上传和重命名选项
- 用户可以设置重命名规则并提交以执行重命名操作
"""

class BatchRenameTool:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        self.files = list(self.folder_path.glob('*.*'))

    def rename_files(self, rename_mode, pattern, replacement, limit=None):
        """
        重命名文件夹中的文件
        
        参数：
        - rename_mode: 重命名模式（'prefix', 'suffix', 'replace'）
        - pattern: 正则表达式模式
        - replacement: 替换字符串
        - limit: 重命名文件的数量限制（None表示无限制）
        
        返回：
        - 成功重命名的文件数量
        """
        renamed_count = 0
        for file in self.files:
            if limit is not None and renamed_count >= limit:
                break
            old_name = str(file)
            new_name = old_name
            if rename_mode == 'prefix':
                new_name = f"{pattern}{file.name}"
            elif rename_mode == 'suffix':
                new_name = f"{file.name}{pattern}"
            elif rename_mode == 'replace':
                new_name = re.sub(pattern, replacement, file.name)
            else:
                continue
            new_path = self.folder_path / new_name
            if old_name != new_name:
                try:
                    os.rename(old_name, str(new_path))
                    renamed_count += 1
                except Exception as e:
                    print(f"Error renaming {old_name} to {new_name}: {e}")
        return renamed_count

# 使用GRADIO创建界面
def get_input():
    folder_path = gr.inputs.Folder(label='Upload a folder')
    rename_mode = gr.inputs.Radio(['prefix', 'suffix', 'replace'], label='Rename mode')
    pattern = gr.inputs.Textbox(label='Pattern')
    replacement = gr.inputs.Textbox(label='Replacement')
    limit = gr.inputs.Number(label='Limit (0 for all)', default=0)
    return folder_path, rename_mode, pattern, replacement, limit

def rename_action(input_args):
    folder_path, rename_mode, pattern, replacement, limit = input_args
    tool = BatchRenameTool(folder_path)
    return tool.rename_files(rename_mode, pattern, replacement, limit)

iface = gr.Interface(
    fn=rename_action,
    inputs=get_input(),
    outputs='text',
    title='Batch File Renamer',
    description='Upload a folder and rename files in batch.'
)
iface.launch()
