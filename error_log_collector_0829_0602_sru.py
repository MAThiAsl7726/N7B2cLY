# 代码生成时间: 2025-08-29 06:02:39
import gr
from gr import Textbox, Text, Download
from datetime import datetime
import os

# 错误日志收集器类
class ErrorLogCollector:
    def __init__(self):
        # 初始化gr.io对象
        self.io = gr.Interface(
            func=self.collect_error_log, 
            inputs=[Textbox(label="Error Log")], 
            outputs=[Text(label="Error collected at"), Download(label="Download Error Log")]
        )
        self.log_file = "error_log.txt"
        self.log_directory = "./logs"

    def collect_error_log(self, error_log):
        # 检查日志目录是否存在，不存在则创建
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)
        
        # 将错误日志写入文件
        with open(os.path.join(self.log_directory, self.log_file), "a") as file:
            file.write(f"{datetime.now()}: {error_log}
")
        
        # 返回收集错误的时间及下载链接
        return datetime.now(), os.path.join(self.log_directory, self.log_file)

    def launch(self):
        # 启动gr界面
        self.io.launch()

# 如果脚本被直接运行，则启动错误日志收集器
if __name__ == '__main__':
    error_log_collector = ErrorLogCollector()
    error_log_collector.launch()