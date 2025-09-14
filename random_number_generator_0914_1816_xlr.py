# 代码生成时间: 2025-09-14 18:16:38
import gradio as gr
def generate_random_number(min_value, max_value):    """
    Generates a random number between min_value and max_value.
    
    Parameters:
    min_value (int): The minimum value of the random number.
    max_value (int): The maximum value of the random number.
    
    Returns:
    int: A random number between min_value and max_value.
    """    
    if min_value >= max_value:
        raise ValueError("min_value must be less than max_value")
    
    return gr.update(value=randint(min_value, max_value))

# Define the interface with Gradio
iface = gr.Interface(
    fn=generate_random_number,
    inputs=[gr.Slider(minimum=0, maximum=100, default=10, label="Minimum Value"),
            gr.Slider(minimum=0, maximum=100, default=20, label="Maximum Value")],
    outputs="number",
    title="Random Number Generator",
    description="Generate a random number between two values."
)

# Run the interface in demo mode
iface.launch()