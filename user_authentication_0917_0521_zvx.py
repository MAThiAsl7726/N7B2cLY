# 代码生成时间: 2025-09-17 05:21:32
import gradio as gr
def authenticate_user(username, password):
    # 模拟的用户数据库
    user_db = {
        "admin": "admin123",
        "user1": "password1"
    }

    try:
        # 检查用户名是否存在
        if username not in user_db:
            return {"success": False, "message": "Username not found"}

        # 检查密码是否正确
        if user_db[username] == password:
            return {"success": True, "message": "Authentication successful"}
        else:
            return {"success": False, "message": "Incorrect password"}

    except Exception as e:
        # 错误处理
        return {"success": False, "message": f"An error occurred: {str(e)}"}

# 创建Gradio接口
iface = gr.Interface(
    fn=authenticate_user,
    inputs=["text", "text"],  # 输入参数
    outputs="json",  # 输出参数
    title="User Authentication",
    description="Authenticate a user with a username and password"
)

if __name__ == '__main__':
    iface.launch()