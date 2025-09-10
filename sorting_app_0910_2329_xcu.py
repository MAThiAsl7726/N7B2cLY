# 代码生成时间: 2025-09-10 23:29:14
import gradio as gr
def sort_numbers(numbers):
    """
    Sorts the list of numbers using the insertion sort algorithm.
    
    Parameters:
    - numbers (list): A list of integers to be sorted.
    
    Returns:
    - list: A sorted list of integers.
    """
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of integers.")
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    
    return numbers

# Create Gradio interface
iface = gr.Interface(
    fn=sort_numbers,
    inputs=gr.Textbox(label="Enter a list of numbers separated by commas (e.g., 34, 7, 23, 32, 5)"),
    outputs="text"
)

if __name__ == "__main__":
    iface.launch()