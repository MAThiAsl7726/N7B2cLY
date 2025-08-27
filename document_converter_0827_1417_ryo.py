# 代码生成时间: 2025-08-27 14:17:28
import gradio as gr
import docx
import os

"""
文档格式转换器

这个程序使用GRADIO框架创建一个简单的界面，
用户可以上传一个.docx文档，并将其转换为.txt格式。
"""
# 改进用户体验

def convert_docx_to_txt(docx_file):
    """
    将.docx文件转换为.txt文件

    参数:
    docx_file: 上传的.docx文件
# 增强安全性

    返回:
    转换后的.txt文件内容
    """
    try:
        # 检查文件是否为空
        if not docx_file:
            return "请选择一个文件"
        
        # 读取.docx文件
        doc = docx.Document(docx_file)
# 增强安全性
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)

        # 将文本内容保存到.txt文件
        txt_filename = os.path.splitext(docx_file.filename)[0] + ".txt"
        with open(txt_filename, 'w', encoding='utf-8') as f:
            f.write('
'.join(full_text))

        # 返回.txt文件内容
# 扩展功能模块
        with open(txt_filename, 'r', encoding='utf-8') as f:
# TODO: 优化性能
            return f.read()
    except Exception as e:
        """
        错误处理
        """
        return f"转换失败: {str(e)}"
# 添加错误处理

# 创建GRADIO界面
iface = gr.Interface(
    fn=convert_docx_to_txt,
    inputs=gr.inputs.File(label="上传.docx文件"),
# 扩展功能模块
    outputs=gr.outputs.Textbox(label="转换结果"),
    title="文档格式转换器",
    description="将.docx文档转换为.txt格式"
)

# 启动GRADIO界面
iface.launch()