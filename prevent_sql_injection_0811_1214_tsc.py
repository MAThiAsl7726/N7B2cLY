# 代码生成时间: 2025-08-11 12:14:38
import sqlite3
from gradio import *

# 函数：防止SQL注入的数据库查询
# 使用参数化查询来防止SQL注入
def safe_query(db_path, query, params):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # 使用参数化查询来防止SQL注入
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        print(f"数据库错误：{e}")
        return None

# 设置Gradio界面
def main():
    input_elements = [
        # 输入框：数据库路径
        components.Textbox(label="数据库路径"),
        # 输入框：SQL查询语句
        components.Textbox(label="SQL查询语句"),
        # 输入框：查询参数（JSON字符串）
        components.Textbox(label="查询参数（JSON字符串）")
    ]
    output_element = components.Textbox(label="查询结果")
    # 创建Gradio界面
    demo = Interface(
        fn=safe_query,
        inputs=input_elements,
        outputs=output_element,
        examples=[
            ("./database.db", "SELECT * FROM users WHERE age > ?", "{"params":[23]}}"),
        ],
        description="防止SQL注入数据库查询"
    )
    demo.launch()

if __name__ == '__main__':
    main()
