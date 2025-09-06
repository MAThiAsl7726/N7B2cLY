# 代码生成时间: 2025-09-07 04:11:20
import gradio as gr
def process_csv(file_path):
    """
    Function to process a CSV file.
    This function reads a CSV file and returns the processed data.
    
    Args:
    file_path (str): The path to the CSV file.
    
    Returns:
    list: A list of dictionaries where each dictionary represents a row in the CSV file.
    """
    try:
        import pandas as pd
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
def batch_process_csv(files):
    """
    Function to batch process multiple CSV files.
    This function takes a list of file paths, processes each file, and returns the results.
    
    Args:
    files (list): A list of paths to CSV files.
    
    Returns:
    list: A list of lists where each list contains the processed data of a CSV file.
    """
    results = []
    for file_path in files:
        result = process_csv(file_path)
        results.append(result)
    return results
def main():
    with gr.Blocks() as demo:
        gr.Markdown("## CSV文件批量处理器")
        gr.Markdown("本程序允许您上传多个CSV文件，并批量处理它们。")
        upload = gr.File(multiple=True)
        process_button = gr.Button("处理CSV文件")
        output = gr.JSON()
        
        def process_csv_files(files):
            return batch_process_csv(files)
        
        process_button.click(process_csv_files, inputs=upload, outputs=output)
        
    demo.launch()
if __name__ == "__main__":
    main()