# 代码生成时间: 2025-09-04 09:45:50
import gradio as gr
def add(x, y):
    """Add two numbers."""
    return x + y
def subtract(x, y):
    """Subtract two numbers."""
    return x - y
def multiply(x, y):
    """Multiply two numbers."""
    return x * y
def divide(x, y):
    """Divide two numbers."""
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
def math_calculator():
    """A calculator that performs basic mathematical operations."""
    with gr.Blocks() as demo:
        # Define the UI elements for each operation
        x = gr.Number(label="First number")
        y = gr.Number(label="Second number")
        add_result = gr.Textbox(label="Add result")
        subtract_result = gr.Textbox(label="Subtract result")
        multiply_result = gr.Textbox(label="Multiply result")
        divide_result = gr.Textbox(label="Divide result")
        
        # Define the buttons for each operation
        add_button = gr.Button("Add")
        subtract_button = gr.Button("Subtract")
        multiply_button = gr.Button("Multiply")
        divide_button = gr.Button("Divide")
        
        # Define the logic for each operation
        add_button.click(fn=add, inputs=[x, y], outputs=add_result)
        subtract_button.click(fn=subtract, inputs=[x, y], outputs=subtract_result)
        multiply_button.click(fn=multiply, inputs=[x, y], outputs=multiply_result)
        divide_button.click(fn=divide, inputs=[x, y], outputs=divide_result)
    return demo
def main():
    """The main function that runs the calculator."""
    calculator = math_calculator()
    calculator.launch()
def __name__ == "__main__":
    main()