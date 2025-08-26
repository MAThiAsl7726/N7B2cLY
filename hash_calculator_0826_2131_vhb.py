# 代码生成时间: 2025-08-26 21:31:40
import hashlib\
from gradio import *

"""
哈希值计算工具
使用GRADIO框架实现一个简单的哈希值计算器，支持多种哈希算法。
"""

# 支持的哈希算法列表\
SUPPORTED_HASHES = ["md5", "sha1", "sha256", "sha512"]\

"""
计算哈希值的函数\
参数：
- text: 需要计算哈希值的字符串\
- hash_type: 使用的哈希算法\
返回值：计算得到的哈希值字符串"""
def calculate_hash(text, hash_type):
    try:
        # 根据选择的哈希算法创建哈希对象
        hash_obj = getattr(hashlib, hash_type)()
        # 对字符串进行编码并计算哈希值
        hash_obj.update(text.encode('utf-8'))
        # 返回计算得到的哈希值字符串
        return hash_obj.hexdigest()
    except AttributeError:
        # 如果选择的哈希算法不受支持，返回错误信息
        return "Unsupported hash type"
    except Exception as e:
        # 处理其他可能的异常
        return str(e)

# 创建GRADIO界面
iface = Interface(
    # 输入字段：接受用户输入的字符串
    fn\=text, 
    # 选择字段：允许用户选择哈希算法
    fn=select, options=SUPPORTED_HASHES, label="Select a hash type",
    # 输出字段：显示计算得到的哈希值
    outputs="text",
    # 设置界面标题和描述
    title="Hash Calculator",
    description="Calculate the hash of a given string using different hash algorithms."
)

"""
在GRADIO界面上运行计算哈希值函数
参数：
- inputs: 包含用户输入的字符串和选择的哈希算法
返回值：计算得到的哈希值字符串"""
def run_hash_calculator(inputs):
    return calculate_hash(inputs[0], inputs[1])

"""
在GRADIO界面上运行应用程序"""
iface.launch(
    server_name="localhost",
    server_port=7860,
    share=False,
    show_error=True,
    css="style.css"
)