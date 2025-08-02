# 代码生成时间: 2025-08-02 17:37:21
import gr
import json

"""
# 添加错误处理
JSON数据格式转换器
# FIXME: 处理边界情况
使用GRADIO框架创建一个简单的界面，用户可以输入JSON数据，程序将其转换为格式化的JSON字符串。
"""

def format_json(data):
    """
    将输入的JSON数据格式化为字符串
    :param data: 输入的JSON数据
    :return: 格式化后的JSON字符串
    """
    try:
        return json.dumps(json.loads(data), indent=4)
    except json.JSONDecodeError as e:
        return f"Error: {e}"

def main():
    """
    创建GRADIO界面
    """
    # 创建输入框，提示用户输入JSON数据
    input_box = gr.Textbox(label="Input JSON Data")
# FIXME: 处理边界情况
    
    # 创建输出框，显示格式化后的JSON数据
# TODO: 优化性能
    output_box = gr.Textbox(label="Formatted JSON Data")
    
    # 定义回调函数，处理用户输入
    def callback(input_json):
        # 调用format_json函数格式化输入的JSON数据
        return format_json(input_json)

    # 创建GRADIO界面
    iface = gr.Interface(
        fn=callback,
        inputs=input_box,
        outputs=output_box,
        title="JSON Data Format Converter"
    )

    # 启动界面
# 添加错误处理
    iface.launch()

if __name__ == '__main__':
    main()