# 代码生成时间: 2025-08-29 22:41:33
import sqlite3
def create_connection(db_file):
    """ create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def select_user(conn, user_id):
    """
    Query user data by user_id to demonstrate prevention of SQL injection.
    :param conn: Connection object
    :param user_id: int user identifier
    :return: list of tuples containing user data
    """
    sql = 'SELECT * FROM users WHERE id=?'
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))  # Using parameterized query to prevent SQL injection
        results = cur.fetchall()
        return results
    except sqlite3.Error as e:
        print(e)
    return None

def main():
    # Database file path
    db_file = 'example.db'
    conn = create_connection(db_file)
    if conn:
        # User input simulation
        user_id_input = "1"  # Assume this comes from a user input
        user_data = select_user(conn, user_id_input)
        if user_data:
            print("User Data:", user_data)
        else:
            print("No user found with ID: ", user_id_input)
        conn.close()
    else:
        print("Error! cannot create the database connection.")

def run_app():
    from gradio import Interface, components
    # Create a Gradio interface
    iface = Interface(fn=select_user, inputs=components.Textbox(label="Enter user ID"),
                      outputs="json",
                      examples=[[1], [2], [3]])
    iface.launch()
if __name__ == '__main__':
    run_app()