# 代码生成时间: 2025-08-12 23:40:48
import gradio as gr
import random

"""
随机数生成器

该程序使用GRADIO框架创建一个简单的随机数生成器。用户可以通过输入最小值和最大值来生成一个随机数。

参数:
    - min_value (int): 最小值
    - max_value (int): 最大值

返回:
    - random_number (int): 生成的随机数
"""

def generate_random_number(min_value, max_value):
    """根据给定的最小值和最大值生成随机数"""
    if min_value > max_value:
        # 如果最小值大于最大值，则抛出异常
        raise ValueError("最小值不能大于最大值")

    # 使用random模块生成随机数
    random_number = random.randint(min_value, max_value)
    return random_number

# 创建Gradio界面
iface = gr.Interface(
    fn=generate_random_number,
    inputs=[
        gr.Textbox(label="最小值", placeholder="输入最小值"),
        gr.Textbox(label="最大值", placeholder="输入最大值")
    ],
    outputs=gr.Textbox(label="随机数"),
    title="随机数生成器",
    description="输入最小值和最大值，生成一个随机数"
)

# 启动Gradio界面
iface.launch()