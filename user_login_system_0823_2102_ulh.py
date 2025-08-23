# 代码生成时间: 2025-08-23 21:02:42
import gradio as gr
def login(username, password):
    # 模拟数据库中的用户名和密码
    # 这里为了示例简单，使用固定的用户名和密码
    # 在实际应用中，应该从数据库或其他存储介质中读取
    correct_username = "admin"
    correct_password = "password123"

    # 检查用户名和密码是否匹配
    if username == correct_username and password == correct_password:
        return "Login successful!"
    else:
        return "Invalid username or password."

# 创建Gradio界面
iface = gr.Interface(
    fn=login,
    inputs=["text", "text"],  # 用户名和密码输入框
    outputs="text",  # 输出结果
    title="User Login System"
)

# 启动Gradio应用
iface.launch()