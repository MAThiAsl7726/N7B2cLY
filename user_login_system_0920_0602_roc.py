# 代码生成时间: 2025-09-20 06:02:13
import gradio as gr
def validate_login(username, password):
    # 用户名和密码验证逻辑
    # 这里使用硬编码的用户名和密码作为示例
    correct_username = "admin"
    correct_password = "password123"
    if username == correct_username and password == correct_password:
        return "Login successful!"
    else:
        return "Invalid username or password."

# 创建Gradio界面
demo = gr.Interface(
    fn=validate_login,
    inputs=["text", "password"],  # 输入框
    outputs="text",  # 输出文本
    title="User Login System",  # 界面标题
    description="Enter your username and password to login."  # 界面描述
)

# 运行Gradio界面
if __name__ == '__main__':
    demo.launch()