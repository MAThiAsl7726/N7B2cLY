# 代码生成时间: 2025-09-15 16:49:55
import gradio as gr
import schedule
import time
from threading import Thread

# 定义定时任务函数
def my_scheduled_job():
    """
    模拟定时任务
    """
    print("定时任务执行中...")

# 定义启动定时任务的函数
def start_scheduler():
    """
    启动定时任务调度器
    """
    schedule.every(10).seconds.do(my_scheduled_job)  # 每10秒执行一次任务
    while True:
        schedule.run_pending()
        time.sleep(1)

# 定义gradio界面
def gr_interface():
    """
    定义GrAIo界面
    """
    with gr.Blocks() as demo:
        # 启动定时任务的按钮
        button = gr.Button("启动定时任务")
        output = gr.Textbox(label="输出")
        
        # 按钮回调函数
        def on_button_click():
            nonlocal thread
            if not thread.is_alive():
                thread = Thread(target=start_scheduler)
                thread.start()
                output.value = "定时任务已启动！"
            else:
                output.value = "定时任务已在运行中..."
        
        button.click(on_button_click, inputs=[], outputs=[output])
    
    # 启动GrAIo界面
    demo.launch()

# 主函数
if __name__ == '__main__':
    thread = None
    try:
        gr_interface()
    except Exception as e:
        print(f"发生错误：{e}")