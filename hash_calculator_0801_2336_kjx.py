# 代码生成时间: 2025-08-01 23:36:29
import hashlib
from gradio import Interface, components

"""
哈希值计算工具
这个程序使用GRADIO框架创建一个简单的哈希值计算工具，
允许用户输入文本并计算其SHA256哈希值。
"""

def calculate_hash(text):
    """
    计算给定文本的SHA256哈希值。
    参数:
    text (str): 要计算哈希值的文本。
    返回:
    str: 文本的SHA256哈希值。
    """
    try:
        # 创建一个sha256哈希对象
        hash_object = hashlib.sha256(text.encode())
        # 获取16进制格式的哈希值
        hash_value = hash_object.hexdigest()
        return hash_value
    except Exception as e:
        # 处理任何可能的错误
        return str(e)

# 创建GRADIO接口
iface = Interface(
    fn=calculate_hash,
    inputs=components.Textbox(label="输入文本"),
    outputs=components.Textbox(label="SHA256哈希值"),
    title="哈希值计算工具",
    description="输入文本并计算其SHA256哈希值。"
)

# 运行GRADIO接口
iface.launch()