# 代码生成时间: 2025-09-10 01:05:29
import hashlib
import gr
from typing import Optional

"""
A simple hash calculator tool using the Gradio framework.
This tool allows users to enter a string and select a hash function to compute the hash value.
"""

def calculate_hash(input_string: str, hash_function: str) -> Optional[str]:
    """
    Calculate the hash of the given input string using the specified hash function.

    Args:
    input_string (str): The string to be hashed.
    hash_function (str): The name of the hash function to use.

    Returns:
    Optional[str]: The hash value of the input string, or None if an error occurs.
    """
    try:
        # Get the hash function from hashlib based on the provided name
        func = getattr(hashlib, hash_function.lower(), None)
        if not func:
            raise ValueError("Unsupported hash function")

        # Compute the hash value
        hash_value = func(input_string.encode()).hexdigest()
        return hash_value
    except Exception as e:
        # Handle any errors that occur during hashing
        print(f"An error occurred: {e}")
        return None

# Define the Gradio interface
iface = gr.Interface(
    fn=calculate_hash,
    inputs=["text", "dropdown"],  # Input text and dropdown for hash function selection
    outputs="text",
    title="Hash Calculator Tool",
    description="Enter a string and select a hash function to compute the hash value.",
    options={
        "text": {
            "label": "Input String",
            "placeholder": "Enter a string..."
        },
        "dropdown": {
            "label": "Hash Function",
            "choices": ["md5", "sha1", "sha256", "sha512"]
        }
    }
)

# Run the Gradio interface
iface.launch()