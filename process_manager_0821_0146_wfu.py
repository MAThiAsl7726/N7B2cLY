# 代码生成时间: 2025-08-21 01:46:26
import psutil
import gradio as gr

# 进程管理器类
class ProcessManager:
    def __init__(self):
        """ 初始化进程管理器 """
        pass
    
    def list_processes(self):
        """ 列出所有进程的基本信息 """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                process_info = proc.info
                processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # 忽略无法访问的进程
                continue
        return processes
    
    def terminate_process(self, pid):
        """ 终止指定进程ID的进程 """
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            return f"Process with PID {pid} terminated."
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return f"Failed to terminate process with PID {pid}."

# 创建Gradio界面
def create_interface():
    """ 创建Gradio界面 """
    pm = ProcessManager()
    
    with gr.Blocks() as demo:
        gr.Markdown("""# 进程管理器
        
        这个工具允许你查看系统中的所有进程，并终止指定的进程。
        """)
        
        process_list = gr.Dropdown(label="Select a process to terminate", choices=[], multiselect=False)
        terminate_button = gr.Button("Terminate Process")
        output = gr.Textbox(label="Result")
        
        def update_process_list():
            """ 更新进程列表 """
            pm.processes = pm.list_processes()
            process_list.choices = [proc['name'] for proc in pm.processes]
            return {}
        
        def on_terminate_click(process_id):
            """ 终止选中的进程 """
            result = pm.terminate_process(process_id)
            output.value = result
            return {}
        
        process_list.change(update_process_list, inputs=[], outputs=process_list)
        terminate_button.click(on_terminate_click, inputs=process_list, outputs=output)
    
    demo.launch()

if __name__ == '__main__':
    create_interface()