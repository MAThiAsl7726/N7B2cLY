# 代码生成时间: 2025-08-07 16:38:42
import gradio as gr
def login(username, password):
    # 模拟的用户数据库
    users = {"user1": "password123", "user2": "myPassword"}
    # 验证用户是否存在及其密码是否正确
    if username in users and users[username] == password:
        return f"Welcome {username}! You have successfully logged in."
    else:
        return "Invalid username or password."

# 使用Gradio创建登录界面
iface = gr.Interface(
    fn=login,
    inputs=["text", "text"],
    outputs="text",
    title="User Login System",
    description="Please enter your username and password to log in."
)

# 运行Gradio界面
iface.launch()