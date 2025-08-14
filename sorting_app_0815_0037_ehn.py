# 代码生成时间: 2025-08-15 00:37:59
import gradio as gr
def get_sorted_list(input_list, algorithm):
    """Sorts the input list using the specified algorithm.

    Args:
        input_list (list): The list of numbers to sort.
        algorithm (str): The sorting algorithm to use ('bubble', 'quick', 'merge').

    Returns:
        list: The sorted list of numbers.
    ""
    try:
        if not input_list or not isinstance(input_list, list) or \
           not all(isinstance(x, (int, float)) for x in input_list):
            raise ValueError("Input list must be a list of numbers.")
        
        if algorithm == 'bubble':
            return bubble_sort(input_list)
        elif algorithm == 'quick':
            return quick_sort(input_list)
        elif algorithm == 'merge':
            return merge_sort(input_list)
        else:
            raise ValueError("Invalid sorting algorithm. Choose 'bubble', 'quick', or 'merge'.")
    except Exception as e:
        return str(e)
def bubble_sort(arr):
    """Performs bubble sort on the input array.

    Args:
        arr (list): The array of numbers to sort.

    Returns:
        list: The sorted array.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def quick_sort(arr):
    """Performs quick sort on the input array.

    Args:
        arr (list): The array of numbers to sort.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def merge_sort(arr):
    """Performs merge sort on the input array.

    Args:
        arr (list): The array of numbers to sort.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]
    return merge(merge_sort(left_half), merge_sort(right_half))
def merge(left, right):
    """Merges two sorted arrays into one sorted array.

    Args:
        left (list): The left sorted array.
        right (list): The right sorted array.

    Returns:
        list: The merged sorted array.
    """
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result
def main():
    with gr.Blocks() as demo:
        gr.Markdown("# Sorting Algorithm App")
        with gr.Row():
            with gr.Column():
                input_list = gr.Number("Enter numbers separated by commas", label="Input List")
                algorithm = gr.Radio(["Bubble Sort", "Quick Sort", "Merge Sort"], label="Algorithm")
            with gr.Column():
                sorted_list = gr.Textbox(label="Sorted List")
        input_list.change(lambda x: get_sorted_list([int(num) for num in x.split(',')], algorithm.value), inputs=[input_list], outputs=[sorted_list])
    demo.launch()
def __main__():
    main()
if __name__ == "__main__":
    __main__()