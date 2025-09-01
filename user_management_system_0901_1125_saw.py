# 代码生成时间: 2025-09-01 11:25:13
import gradio as gr

# 用户权限管理系统
class UserManagementSystem:
    def __init__(self):
        # 初始化用户数据
        self.user_data = {
            "admin": {"username": "admin", "password": "admin123", "roles": ["admin"], "permissions": ["create_user", "delete_user