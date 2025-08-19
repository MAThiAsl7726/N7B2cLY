# 代码生成时间: 2025-08-19 19:52:27
import gradio as gr
def authenticate_user(username, password):
    """
    Authenticates a user based on their username and password.
    
    Args:
        username (str): The username of the user.
        password (str): The password of the user.
    
    Returns:
        dict: A dictionary containing the authentication status and message.
    """
    # Mock user database
    user_db = {
        "user1": "password1",
        "user2": "password2"
    }
    
    # Check if the user exists in the database
    if username in user_db:
        # Check if the password is correct
        if user_db[username] == password:
            return {"status": "success", "message": "Authentication successful."}
        else:
            return {"status": "error", "message": "Incorrect password."}
    else:
        return {"status": "error", "message": "User not found."}

# Create a Gradio interface for the authentication function
iface = gr.Interface(
    fn=authenticate_user,
    inputs=[gr.Textbox(label="Username"), gr.Textbox(label="Password", type="password")],
    outputs="text"
)

# Launch the interface
iface.launch()