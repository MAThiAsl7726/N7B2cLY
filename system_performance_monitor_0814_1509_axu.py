# 代码生成时间: 2025-08-14 15:09:33
import psutil
import gr
from gr import Title, Data, File, Button, Download

# Class to monitor system performance
class SystemPerformanceMonitor:
    def __init__(self):
        self._cpu_usage = psutil.cpu_percent(interval=1)
        self._memory_usage = psutil.virtual_memory().percent

    def get_cpu_usage(self):
        """Returns the CPU usage percentage"""
        return self._cpu_usage

    def get_memory_usage(self):
        """Returns the memory usage percentage"""
        return self._memory_usage

# Function to setup the Gradio interface
def setup_gr_interface():
    title = Title("System Performance Monitor")
    input_button = Button("Refresh Stats")
    output_cpu = Data(label="CPU Usage")
    output_memory = Data(label="Memory Usage")
    download_button = Button("Download Report")

    # Function to refresh stats when the button is clicked
    def refresh_stats(input):
        monitor = SystemPerformanceMonitor()
        output_cpu.update(value=str(monitor.get_cpu_usage()) + "%")
        output_memory.update(value=str(monitor.get_memory_usage()) + "%")
        return str(monitor.get_cpu_usage()) + "%", str(monitor.get_memory_usage()) + "%"

    # Function to generate and download a report when the button is clicked
    def download_report():
        monitor = SystemPerformanceMonitor()
        report = f"CPU Usage: {monitor.get_cpu_usage()}%\
Memory Usage: {monitor.get_memory_usage()}%"
        return report

    # Create the Gradio interface
    iface = gr.Interface(
        fn=refresh_stats,
        inputs=input_button,
        outputs=[output_cpu, output_memory],
        live=True
    )

    # Add a download button
    iface.add_component(download_button, outputs=[File(label="Download Report", file_type="text/plain