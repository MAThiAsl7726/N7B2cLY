# 代码生成时间: 2025-08-12 10:49:28
import gradio as gr
def theme_switcher(theme_id):
    """
    Function to switch between different themes.
    Args:
        theme_id (int): The ID of the theme to switch to.
    Returns:
        str: A message indicating the theme has been switched.
    """
    try:
        # Define available themes
        themes = {
            1: 'Light',
            2: 'Dark',
            3: 'High Contrast'
        }

        # Check if the theme_id is valid
        if theme_id not in themes:
            return "Invalid theme ID. Please choose a valid theme."

        # Switch to the selected theme
        theme_name = themes[theme_id]
        return f"Theme switched to {theme_name}."

    except Exception as e:
        return f"An error occurred: {str(e)}."

def main():
    # Create a Gradio interface
    theme_switcher_interface = gr.Interface(
        fn=theme_switcher,
        inputs=gr.Slider(minimum=1, maximum=3, step=1, label="Select Theme"),
        outputs="text",
        live=True
    )
    theme_switcher_interface.launch()

def __name__ == "__main__":
    main()