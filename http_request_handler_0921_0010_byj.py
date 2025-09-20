# 代码生成时间: 2025-09-21 00:10:16
import requests
from gradio import Interface

"""
HTTP请求处理器模块，使用GRADIO框架创建HTTP请求界面。
"""

def make_http_request(url, method):
    """
    发送HTTP请求到指定的URL
    
    参数:
    url (str): 要请求的URL地址
    method (str): 请求方法，例如'GET', 'POST', 'PUT', 'DELETE'
    
    返回:
    str: HTTP响应的文本内容
    
    抛出:
    Exception: 请求过程中发生的任何异常
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'POST':
            response = requests.post(url)
        elif method.upper() == 'PUT':
            response = requests.put(url)
        elif method.upper() == 'DELETE':
            response = requests.delete(url)
        else:
            raise ValueError('不支持的请求方法')
        
        response.raise_for_status()  # 抛出HTTPError异常，如果HTTP请求返回一个失败状态
        return response.text
    except requests.RequestException as e:
        raise Exception(f'HTTP请求失败: {e}')

"""
创建GRADIO界面
"""
iface = Interface(
    fn=make_http_request,
    inputs=["text", "text"],  # URL和方法输入
    outputs="text",  # 响应输出
    examples=[["https://www.example.com", "GET"]],
    title="HTTP请求处理器",
    description="通过输入URL和HTTP方法发送请求，并显示响应。"
)

# 运行GRADIO界面
iface.launch()