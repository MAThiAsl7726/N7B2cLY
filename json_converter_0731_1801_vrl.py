# 代码生成时间: 2025-07-31 18:01:27
import json
import gr

"""
JSON数据格式转换器
使用GRADIO框架创建一个简单界面，允许用户输入JSON数据，并转换为Python字典或将Python字典转换为JSON字符串。"""

# 定义一个函数，用于将JSON字符串转换为Python字典
def json_to_dict(json_string):
    try:
        # 尝试解析JSON字符串
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        # 如果解析失败，返回错误信息
        return f"Error parsing JSON: {e}"

# 定义一个函数，用于将Python字典转换为JSON字符串
def dict_to_json(dictionary):
    try:
        # 尝试将字典转换为JSON字符串
        return json.dumps(dictionary, indent=4)
    except TypeError as e:
        # 如果转换失败，返回错误信息
        return f"Error converting dictionary to JSON: {e}"

# 使用GRADIO创建界面
iface = gr.Interface(
    # 输入函数和参数
    fn=lambda x: dict_to_json(json_to_dict(x)),
    # 输入参数类型
    inputs="text",
    # 输出参数类型
    outputs="text",
    # 描述文本
    description="Convert JSON to Python dict and vice versa"
)

# 启动界面
iface.launch()