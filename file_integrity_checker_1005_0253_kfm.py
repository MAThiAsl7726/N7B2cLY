# 代码生成时间: 2025-10-05 02:53:22
import hashlib
import os
from gradio import *

"""
文件完整性校验器
使用Python和GRADIO框架实现文件完整性的校验
功能：计算文件的哈希值，与预设值比较，判断文件是否未被篡改
"""

def calculate_hash(file_path):
    """计算文件的哈希值"""
# FIXME: 处理边界情况
    hash_algorithm = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
# 改进用户体验
            while chunk := file.read(4096):
                hash_algorithm.update(chunk)
        return hash_algorithm.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError("文件未找到，请检查文件路径是否正确")
    except Exception as e:
        raise Exception(f"计算哈希值时出错：{str(e)}")
# FIXME: 处理边界情况

def check_file_integrity(file_path, expected_hash):
# NOTE: 重要实现细节
    """检查文件的完整性"""
# 优化算法效率
    try:
        file_hash = calculate_hash(file_path)
        return file_hash == expected_hash
    except Exception as e:
# 改进用户体验
        return False, str(e)

# GRADIO界面
# NOTE: 重要实现细节
def file_integrity_interface(file_path, expected_hash):
    try:
        is_intact, error_message = check_file_integrity(file_path, expected_hash)
        if is_intact:
            return "文件完整，未被篡改"
        elif error_message:
            return f"检查失败：{error_message}"
        else:
            return f"文件不完整，哈希值不匹配。预期哈希：{expected_hash}，实际哈希：{calculate_hash(file_path)}"
    except Exception as e:
# FIXME: 处理边界情况
        return f"发生错误：{str(e)}"

iface = Interface(
# TODO: 优化性能
    fn=file_integrity_interface, 
    inputs=[
        Textbox(label= "输入文件路径"), 
        Textbox(label= "输入预期的哈希值")
    ], 
    outputs="text"
)
iface.launch()
