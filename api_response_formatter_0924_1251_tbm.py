# 代码生成时间: 2025-09-24 12:51:54
import json
from gradio import *

"""
API响应格式化工具
=====================================

这个工具允许用户输入原始API响应，并将其格式化为更易读的JSON格式。
=====================================
"""

def format_api_response(response: str) -> str:
    """
    格式化API响应
# NOTE: 重要实现细节
    
    Args:
        response (str): 原始API响应字符串
    
    Returns:
        str: 格式化后的JSON字符串
    
    Raises:
# 扩展功能模块
        ValueError: 如果输入的响应不是有效的JSON
    """
    try:
# 改进用户体验
        # 尝试将输入字符串解析为JSON
        json_data = json.loads(response)
# 增强安全性
        # 将JSON数据序列化为格式化的字符串
        formatted_response = json.dumps(json_data, indent=4)
        return formatted_response
    except json.JSONDecodeError as e:
        # 如果解析失败，抛出ValueError异常
        raise ValueError("Invalid JSON input") from e

# 创建一个Gradio界面
iface = Interface(
    # 输入框，用户可以在这里输入原始API响应
# 增强安全性
    fn=format_api_response,
# NOTE: 重要实现细节
    # 输入框的配置
    inputs="text",
    # 输出框的配置
    outputs="text",
    # 界面标题
    title="API Response Formatter",
# 扩展功能模块
    # 界面描述
    description="Format your API responses into readable JSON."
)

# 启动界面
# 增强安全性
iface.launch()
