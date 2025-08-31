# 代码生成时间: 2025-08-31 13:06:42
import gradio as gr
def validate_data(input_data):
    # 定义验证规则
    valid_data = True
    errors = []
    # 验证字段1：姓名
    if not input_data['name']:
        valid_data = False
        errors.append('Name is required.')
    # 验证字段2：年龄，必须大于0小于100
    if input_data['age'] <= 0 or input_data['age'] >= 100:
        valid_data = False
        errors.append('Age must be between 1 and 99.')
    # 返回验证结果和错误信息
    return {'is_valid': valid_data, 'errors': errors} 

def main():
    # 创建一个表单，其中包含姓名和年龄字段
    with gr.Blocks() as demo:
        gr.Markdown("## Data Validation Demo")
        form = gr.Form([
            "name",   # 姓名字段
            "age"     # 年龄字段
        ], validate_data)
        form.launch()

if __name__ == "__main__":
    main()
