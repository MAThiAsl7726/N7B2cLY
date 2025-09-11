# 代码生成时间: 2025-09-11 20:48:03
import json
from gradio import Interface, Text

"""
JSON数据格式转换器

这个程序使用GRADIO框架来创建一个用户界面，允许用户输入JSON格式的数据，并将其转换为不同的格式。
"""

def json_to_dict(json_data):
    """将JSON字符串转换为Python字典。
    
    参数:
    json_data (str): JSON格式的字符串。
    
    返回:
    dict: Python字典。
    
    异常:
    ValueError: 如果输入的JSON数据无效。
    """
    try:
        data_dict = json.loads(json_data)
        return data_dict
    except json.JSONDecodeError as e:
        raise ValueError("无效的JSON数据: " + str(e))


def dict_to_json(data_dict):
    """将Python字典转换为JSON字符串。
    
    参数:
    data_dict (dict): Python字典。
    
    返回:
    str: JSON格式的字符串。
    """
    return json.dumps(data_dict, indent=4)


def main(json_data):
    """
    主函数，用于转换JSON数据格式。
    
    参数:
    json_data (str): 输入的JSON数据。
    
    返回:
    str: 转换后的JSON字符串。
    """
    data_dict = json_to_dict(json_data)
    json_string = dict_to_json(data_dict)
    return json_string

if __name__ == "__main__":
    # 创建GRADIO界面
    demo = Interface(
        fn=main, 
        inputs=Text(label="输入JSON数据"), 
        outputs="text", 
        title="JSON数据格式转换器", 
        description="在这个界面中，你可以输入JSON格式的数据，程序将自动将其转换为不同的格式。"
    )
    # 运行GRADIO界面
    demo.launch()