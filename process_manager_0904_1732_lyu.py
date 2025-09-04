# 代码生成时间: 2025-09-04 17:32:26
import psutil
import gradio as gr
def get_process_list():
    """
    Fetches the list of all processes and their details.
    
    Returns:
        list: A list of dictionaries where each dictionary contains the details of a process.
    """
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status', 'username']):
        try:
            process_info = proc.info
            processes.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def kill_process(process_id, signal=9):
    """
    Kills a process by its ID.
    
    Args:
        process_id (int): The ID of the process to kill.
        signal (int): The signal to send to the process. Default is SIGKILL (9).
    
    Returns:
        bool: True if the process was successfully killed, False otherwise.
    """
    try:
        process = psutil.Process(process_id)
        process.send_signal(signal)
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def main():
    """
    Main function that sets up the Gradio interface.
    """
    process_list_button = gr.Button("List Processes")
    kill_button = gr.Button("Kill Process")
    process_id_input = gr.Textbox(label="Process ID", placeholder="Enter process ID")
    signal_input = gr.Textbox(label="Signal", placeholder="Enter signal (default 9)", default="9")
    output = gr.Textbox(label="Output")
    process_list_output = gr.Dataframe(label="Process List")
    
    def update_process_list():
        return get_process_list()
    
    def kill_selected_process(process_id, signal):
        result = kill_process(int(process_id), int(signal))
        return "Process killed" if result else "Failed to kill process"
    
    process_list_button.click(fn=update_process_list, outputs=process_list_output)
    kill_button.click(
        fn=kill_selected_process, 
        inputs=[process_id_input, signal_input], 
        outputs=output
    )
    
    demo = gr.Interface(
        fn=None,
        inputs=[process_list_button, kill_button, process_id_input, signal_input],
        outputs=[process_list_output, output],
        live=True
    )
    demo.launch()

if __name__ == "__main__":
    main()