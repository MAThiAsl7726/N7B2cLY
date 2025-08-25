# 代码生成时间: 2025-08-26 07:03:32
import gradio as gr
def generate_test_data(n):
    # 这个函数生成n个测试数据，每个数据是一个包含姓名和年龄的字典
    test_data = []
    for i in range(n):
        name = f"person{i+1}"
        age = i % 50 + 18  # 年龄在18到68之间
        test_data.append({"name": name, "age": age})
    return test_data

# 创建Gradio接口
iface = gr.Interface(
    fn=generate_test_data,  # 要运行的函数
    inputs=gr.inputs.Number(label="Number of test data"),  # 输入参数，用户输入测试数据的数量
    outputs="json",  # 输出参数，输出生成的测试数据列表
    title="Test Data Generator",  # 界面标题
    description="Generate test data using Gradio."  # 界面描述
)

# 启动Gradio界面
iface.launch()
