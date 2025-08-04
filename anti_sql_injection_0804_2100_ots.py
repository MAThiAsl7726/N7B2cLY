# 代码生成时间: 2025-08-04 21:00:59
import gradio as gr
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
# 添加错误处理
    return conn


def execute_query(conn, query, parameters):
# 添加错误处理
    """
    Execute a SQL query with parameters to prevent SQL injection.
# TODO: 优化性能
    :param conn: Connection to the SQLite database.
    :param query: SQL query string.
    :param parameters: Tuple of parameters to be passed to the query.
# 添加错误处理
    :return: Result of the query execution.
    """
# 扩展功能模块
    try:
        cur = conn.cursor()
        cur.execute(query, parameters)
        result = cur.fetchall()
        return result
    except Error as e:
        print(f"An error occurred: {e}")


def main():
    # Connect to the SQLite database
    database = "example.db"
    conn = create_connection(database)
# TODO: 优化性能

    if conn is not None:
        # GRADIO interface
        input_dropdown = gr.Dropdown(label="Choose an action", choices=["SELECT", "INSERT", "UPDATE", "DELETE"])
        input_text = gr.Textbox(label="Input your query parameters (comma-separated)")
        submit = gr.Button("Submit")

        # Define functions for each action
        def handle_select(params):
# 扩展功能模块
            return execute_query(conn, "SELECT * FROM users", (params,))
# FIXME: 处理边界情况

        def handle_insert(params):
            return execute_query(conn, "INSERT INTO users (name, email) VALUES (?, ?)", (params.split(",")[0], params.split(",")[1]))

        def handle_update(params):
            return execute_query(conn, "UPDATE users SET email = ? WHERE name = ?", (params.split(",")[1], params.split(",")[0]))

        def handle_delete(params):
            return execute_query(conn, "DELETE FROM users WHERE name = ?", (params,))
# NOTE: 重要实现细节

        # Configure the GRADIO interface
# NOTE: 重要实现细节
        demo = gr.Interface(
            fn=lambda x, y: {
                "SELECT": handle_select(y),
                "INSERT": handle_insert(y),
                "UPDATE": handle_update(y),
                "DELETE": handle_delete(y)
            }[input_dropdown.value],
            inputs=[input_dropdown, input_text],
            outputs="data",
            title="Anti SQL Injection Demo",
            description="This demo prevents SQL injection by using parameterized queries."
        )

        demo.launch()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()