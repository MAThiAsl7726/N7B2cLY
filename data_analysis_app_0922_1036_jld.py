# 代码生成时间: 2025-09-22 10:36:19
import gradio as gr
import pandas as pd
import numpy as np
from scipy import stats

"""
统计数据分析器
使用GRADIO框架创建的简单应用，用于分析和显示数据的统计信息。
"""

def load_data(file):
    """
    加载数据文件
    
    参数:
        file: 上传的数据文件
    """
    try:
        data = pd.read_csv(file)
        return data
    except Exception as e:
        return str(e)

def calculate_statistics(data):
    """
    计算并返回统计数据
    
    参数:
        data: 包含数据的Pandas DataFrame
    """
    stats_dict = {}
    stats_dict['mean'] = data.mean()
    stats_dict['median'] = data.median()
    stats_dict['std_dev'] = data.std()
    stats_dict['min'] = data.min()
    stats_dict['max'] = data.max()
    return stats_dict

def display_statistics(stats):
    """
    显示统计信息
    
    参数:
        stats: 包含统计数据的字典
    """
    return stats

# 创建GRADIO界面
iface = gr.Interface(
    fn=calculate_statistics,  # 函数
    inputs=gr.File(label="Upload data file"),  # 输入：文件上传组件
    outputs="json",  # 输出：JSON格式
    title="Statistical Data Analyzer",
    description="Upload your data file to analyze its statistical properties."
)

# 启动应用
iface.launch()
