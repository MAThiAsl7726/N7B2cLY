# 代码生成时间: 2025-08-31 17:29:10
import gradio as gr
def responsive_layout_demo(input_text):
    # 响应式布局演示函数
    # input_text: 用户输入的文本
    # 将文本转换为大写并返回
    return input_text.upper()

# 初始化Gradio接口
iface = gr.Interface(
    fn=responsive_layout_demo,
    inputs=gr.Textbox(label="输入文本"),
    outputs="text",
    title="响应式布局设计"
)

# 设置响应式布局参数
iface.layout = "horizontal"  # 设置布局为水平布局
iface.update_layout(height=300)  # 设置组件的高度
iface.update_layout(width=600)  # 设置组件的宽度

# 启动应用
iface.launch()