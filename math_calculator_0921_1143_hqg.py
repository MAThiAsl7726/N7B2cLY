# 代码生成时间: 2025-09-21 11:43:16
import gradio as gr

# 定义数学计算工具集类
class MathCalculator:
    def __init__(self):
        # 这里可以包含类的初始化代码
        pass

    # 加法计算
    def add(self, x, y):
        """
        计算两个数的和
        :param x: 第一个加数
        :param y: 第二个加数
        :return: 两数之和
        """
        try:
            return float(x) + float(y)
        except ValueError:
            # 错误处理，非数字输入
            return "Please enter valid numbers."

    # 减法计算
    def subtract(self, x, y):
        """
        计算两个数的差
        :param x: 被减数
        :param y: 减数
        :return: 两数之差
        """
        try:
            return float(x) - float(y)
        except ValueError:
            return "Please enter valid numbers."

    # 乘法计算
    def multiply(self, x, y):
        """
        计算两个数的积
        :param x: 第一个因数
        :param y: 第二个因数
        :return: 两数之积
        """
        try:
            return float(x) * float(y)
        except ValueError:
            return "Please enter valid numbers."

    # 除法计算
    def divide(self, x, y):
        """
        计算两个数的商
        :param x: 被除数
        :param y: 除数
        :return: 两数之商
        """
        try:
            if y == 0:
                return "Cannot divide by zero."
            return float(x) / float(y)
        except ValueError:
            return "Please enter valid numbers."

# 创建MathCalculator实例
calculator = MathCalculator()

# 定义Gradio接口
iface = gr.Interface(
    # 定义输入输出组件
    fn=calculator.add, 
    inputs=[gr.Textbox(label="Number 1"), gr.Textbox(label="Number 2")],
    outputs="text", 
    # 定义组件标签
    title="Addition Calculator",
    description="Calculates the sum of two numbers"
)

# 运行Gradio接口
iface.launch()