# 代码生成时间: 2025-09-17 11:54:58
import json
import gradio as gr
def json_data_converter(input_data):
    """Converts input data to JSON format and back to string."""
    try:
        # Attempt to parse the input data as JSON
        json_data = json.loads(input_data)
    except json.JSONDecodeError:
        # If there's an error in parsing, return an error message
        return "Error: Input data is not valid JSON."
    try:
        # Convert the JSON data back to a string
        output_data = json.dumps(json_data, indent=4)
    except (TypeError, OverflowError):
        # Handle any other errors that may occur during JSON conversion
        return "Error: Failed to convert JSON data back to string."
    return output_data

# Create the Gradio interface
iface = gr.Interface(
    json_data_converter,
    "text",
    "text",
    examples=["{"key": "value"}"],
    description="This app converts JSON data to string format and back.",
    title="JSON Data Format Converter"
)

# Run the Gradio interface
iface.launch()