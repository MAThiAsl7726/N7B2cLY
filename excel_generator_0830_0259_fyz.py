# 代码生成时间: 2025-08-30 02:59:05
import gradio as gr
import pandas as pd
from openpyxl import Workbook

"""
Excel表格自动生成器

本程序使用GRADIO框架，创建一个简易的Excel表格生成器。
用户可以通过GUI界面输入数据，系统会自动生成Excel表格并下载。

主要功能：
- 接收用户输入的数据
- 生成Excel表格
- 提供表格下载链接

参数说明：
- 输入参数：用户输入的数据，格式为字典（key-value对）
- 输出参数：生成的Excel表格文件
"""

# 定义生成Excel表格的函数
def generate_excel(data):
    try:
        # 创建一个新的Excel工作簿
        wb = Workbook()
        ws = wb.active
        ws.title = 'Sheet1'
        
        # 将用户输入的数据写入Excel表格
        for key, value in data.items():
            ws.append([key, value])
        
        # 保存Excel文件
        filename = 'generated_excel.xlsx'
        wb.save(filename)
        return filename
    except Exception as e:
        # 错误处理
        print(f'生成Excel表格时出错：{e}')
        return None

# 定义GRADIO界面
def main():
    with gr.Blocks() as demo:
        # 创建输入框
        input_data = gr.Textbox(label='请输入数据（格式为key:value）')
        
        # 创建按钮，点击后生成Excel表格
        button = gr.Button('生成Excel表格')
        
        # 创建下载链接
        output = gr.Textbox(label='下载链接')
        
        # 注册回调函数
        button.click(generate_excel, inputs=input_data, outputs=output)
        
    # 启动GRADIO界面
    demo.launch()

if __name__ == '__main__':
    main()