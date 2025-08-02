# 代码生成时间: 2025-08-03 03:19:41
import requests
from grradio import Interface

"""
网络连接状态检查器
使用GRADIO框架创建一个界面，使用户能够检查网络连接状态
"""

def check_connection(url):
    """
    检查网络连接状态
    
    参数：
    url : str
        要检查的URL
    
    返回：
    bool
        如果连接成功返回True，否则返回False
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"检查{url}时发生错误：{e}")
        return False

"""GRADIO界面"""
def grradio_interface():
    """
    创建GRADIO界面
    """
    # 创建Interface实例
    demo = Interface(
        fn=check_connection,
        inputs="text",
        outputs="boolean",
        title="网络连接状态检查器",
        description="输入一个URL来检查网络连接状态",
    )

    # 运行界面
    demo.launch()

"""主函数"""
if __name__ == '__main__':
    grradio_interface()