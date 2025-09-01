# 代码生成时间: 2025-09-01 15:55:38
import gradio as gr

# 导入必要的库
from html import escape
import re

# 定义一个函数来检测和清理XSS攻击脚本
def clean_xss(input_text):
    # 替换HTML实体
    input_text = input_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # 清除JavaScript事件处理函数
    input_text = re.sub(r"(on|xmlns)[^=]*=([^\"']*|[^\"']+)[^>]*", "", input_text)
    # 清除JavaScript标签
    input_text = re.sub(r"<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>"