# 代码生成时间: 2025-09-22 00:28:13
import gradio as gr
def generate_excel(input_data):
    # 导入库
    from openpyxl import Workbook

    # 创建一个新的workbook并添加一个worksheet
    wb = Workbook()
    ws = wb.active

    # 将输入数据写入Excel
    for i, row in enumerate(input_data, start=1):
        for j, value in enumerate(row, start=1):
            ws.cell(row=i, column=j, value=value)

    # 保存Excel文件
    wb.save("github_data.xlsx")
    return "Excel文件已生成"

# 创建Gradio界面
iface = gr.Interface(
    fn=generate_excel, 
    inputs=gr.Textbox(label="输入数据", placeholder="输入数据，用逗号分隔"), 
    outputs="text", 
    title="Excel表格自动生成器", 
    description="输入数据，自动生成Excel表格"
)

# 运行界面
iface.launch()