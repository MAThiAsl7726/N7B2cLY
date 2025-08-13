# 代码生成时间: 2025-08-13 10:37:12
import hashlib
from gradio import interfaces, gradio

"""
哈希值计算工具
================

本程序使用GRADIO框架实现一个简单的哈希值计算工具，支持多种哈希算法。
用户可以通过输入框输入需要计算哈希值的字符串，选择哈希算法，点击计算按钮来得到结果。
"""

class HashCalculator:
    def __init__(self):
        # 定义支持的哈希算法
        self.supported_algorithms = [
            "md5",
            "sha1",
            "sha256",
            "sha512"
        ]
    
def calculate_hash(self, input_string, algorithm):
    """
    计算输入字符串的哈希值

    :param input_string: 需要计算哈希值的字符串
    :param algorithm: 哈希算法名称
    :return: 哈希值字符串
    """
    try:
        # 检查算法是否支持
        if algorithm not in self.supported_algorithms:
            raise ValueError(f"不支持的哈希算法: {algorithm}")

        # 创建哈希对象
        hash_obj = hashlib.new(algorithm)

        # 更新哈希对象
        hash_obj.update(input_string.encode())

        # 返回哈希值
        return hash_obj.hexdigest()
    except Exception as e:
        # 错误处理
        return str(e)

def main():
    # 初始化哈希计算器
    hash_calculator = HashCalculator()

    # 创建GRADIO接口
    demo = gradio.Interface(
        fn=hash_calculator.calculate_hash,
        inputs=[interfaces.Textbox(label="输入字符串"),
                interfaces.Dropdown(label="选择哈希算法", choices=hash_calculator.supported_algorithms)],
        outputs="text",
        title="哈希值计算工具",
        description="计算输入字符串的哈希值"
    )

    # 启动GRADIO应用
    demo.launch()

def __name__ == "__main__":
    main()