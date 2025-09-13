# 代码生成时间: 2025-09-13 08:53:44
import gradio as gr
import random

"""
Random Number Generator using Gradio framework.
This script creates an interactive interface to generate random numbers between a user-specified range.
"""

# Function to generate a random number within a given range
def generate_random_number(min_value, max_value):
    """
    Generate a random number between min_value and max_value.
    
    Parameters:
    min_value (int): The minimum value of the range.
    max_value (int): The maximum value of the range.
    
    Returns:
    int: A random number within the specified range.
    
    Raises:
    ValueError: If min_value is greater than max_value.
    """
    if min_value > max_value:
        raise ValueError("Minimum value cannot be greater than maximum value.")
    return random.randint(min_value, max_value)

# Create a Gradio interface for the random number generator
iface = gr.Interface(
    
    fn=generate_random_number,  # Function to be called
    inputs=[
        gr.Slider(minimum=1, maximum=100, default=1, label="Minimum Value"),
        gr.Slider(minimum=1, maximum=100, default=100, label="Maximum Value")
    ],
    outputs="number",  # Output type
    title="Random Number Generator",
    description="Generate a random number between two specified values."
)

# Launch the Gradio interface
iface.launch()