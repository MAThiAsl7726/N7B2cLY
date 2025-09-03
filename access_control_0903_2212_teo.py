# 代码生成时间: 2025-09-03 22:12:24
import gradio as gr
def authenticate(username, password):
    # 这里使用简单的用户名和密码验证，实际应用中应该使用更安全的验证方式
    correct_username = "admin"
    correct_password = "password123"
    if username == correct_username and password == correct_password:
        return "Access granted"
    else:
        raise ValueError("Invalid username or password")


def main():
    # 创建接口
    demo = gr.Interface(
        fn=authenticate,
        inputs=[gr.Textbox(label="Username"), gr.Textbox(label="Password"),],
        outputs="text"
    )
    # 启动应用
    demo.launch()

if __name__ == "__main__":
    main()
# 改进用户体验
