# 代码生成时间: 2025-09-12 12:53:49
import time
import requests
from requests.exceptions import RequestException
import gr
import gradio as gr

"""
性能测试脚本

该脚本使用GRADIO框架创建一个简单的性能测试应用程序。
它允许用户输入一个URL，并发送请求以测试性能。

功能：
- 发送GET请求到指定的URL
- 记录并显示请求的响应时间和状态码
"""

def test_performance(url):
    """测试指定URL的性能"""
    try:
        # 发送GET请求
        response = requests.get(url)
        # 计算响应时间
        response_time = response.elapsed.total_seconds()
        # 获取状态码
        status_code = response.status_code
        return {
            "response_time": response_time,
            "status_code": status_code,
            "url": url
        }
    except RequestException as e:
        # 处理请求异常
        return {"error": str(e)}

# 创建GRADIO接口
iface = gr.Interface(
    fn=test_performance,
    inputs=gr.Textbox(label="输入URL"),
    outputs=gr.Textbox(label="性能测试结果"),
    examples=["https://www.example.com"],
    title="性能测试脚本",
    description="测试指定URL的响应时间和状态码"
)

# 运行GRADIO应用程序
iface.launch()