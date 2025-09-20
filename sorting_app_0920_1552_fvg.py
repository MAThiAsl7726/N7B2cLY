# 代码生成时间: 2025-09-20 15:52:48
import gradio as gr
def bubble_sort(arr):
    # 实现冒泡排序算法
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def selection_sort(arr):
    # 实现选择排序算法
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def insertion_sort(arr):
    # 实现插入排序算法
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
def merge_sort(arr):
    # 实现归并排序算法
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
def sort_algorithm(input_data, algorithm):
    # 根据用户选择的排序算法进行排序
    if algorithm == "Bubble Sort":
        return bubble_sort(input_data)
    elif algorithm == "Selection Sort":
        return selection_sort(input_data)
    elif algorithm == "Insertion Sort":
        return insertion_sort(input_data)
    elif algorithm == "Merge Sort":
        return merge_sort(input_data)
    else:
        raise ValueError("Invalid sorting algorithm selected.")
def main():
    # 使用Gradio框架创建GUI界面
    demo = gr.Interface(
        fn=sort_algorithm,
        inputs=[gr.Textbox(label="Enter numbers separated by commas"), gr.Radio(["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort"], label="Select an algorithm")],
        outputs="text",
        title="Sorting Algorithm Demo",
        description="Select an algorithm and enter numbers to sort."
    )
    demo.launch()
if __name__ == "__main__":
    main()