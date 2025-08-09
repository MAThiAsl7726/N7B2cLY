# 代码生成时间: 2025-08-09 12:50:33
import requests
from gradio.inputs import TextBox, Number, Dropdown
from gradio.outputs import Label
import json

# 定义API响应格式化工具类
class ApiResponseFormatter:
    def __init__(self, api_url):
        """
        类的初始化方法，存储API的URL。
        :param api_url: API的URL字符串
        """
        self.api_url = api_url

    def fetch_api_response(self, params):
        """
        从API获取响应。
        :param params: 用于API请求的参数字典。
        :return: API响应的JSON对象。
        """
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API请求失败: {e}")
            return None

    def format_response(self, response):
        """
        格式化API响应。
        :param response: API响应的JSON对象。
        :return: 格式化后的字符串。
        """
        if response is None:
            return "API响应为空或请求失败。"
        try:
            formatted_response = json.dumps(response, indent=4, ensure_ascii=False)
            return formatted_response
        except TypeError as e:
            print(f"格式化响应失败: {e}")
            return "格式化响应失败。"

# Gradio界面设置
def setup_gradio_interface():
    """
    设置和启动Gradio界面。
    """
    with gr.Interface(
        fn=format_response, 
        inputs=[TextBox(label="API URL"),
                TextBox(label="Parameters (JSON)"),
                Dropdown(label="Format Option", choices=["Pretty Print", "Compact"])], 
        outputs=Label(label="Formatted API Response"),
        examples=[["https://jsonplaceholder.typicode.com/todos/1", "{"userId": 1, "completed": false}", "Pretty Print"],
                  ["https://jsonplaceholder.typicode.com/todos/1", "{"userId": 1, "completed": false}", "Compact"]],
    ) as demo:
        demo.launch()

if __name__ == "__main__":
    setup_gradio_interface()