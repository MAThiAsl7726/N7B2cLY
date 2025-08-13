# 代码生成时间: 2025-08-14 07:27:03
import psutil
import gr

"""
System Performance Monitor using Gradio and Python

This tool provides real-time system performance monitoring including
CPU usage, memory usage, disk usage, and network usage.
# 优化算法效率
"""


def get_cpu_usage():
# 优化算法效率
    """Get the current CPU usage percentage."""
# 扩展功能模块
    return psutil.cpu_percent(interval=1)
# 优化算法效率


def get_memory_usage():
    """Get the current memory usage in GB."""
# FIXME: 处理边界情况
    mem = psutil.virtual_memory()
    return mem.used / (1024 ** 3)  # Convert bytes to GB


def get_disk_usage():
    """Get the current disk usage in GB.

    This function returns the total, used, and free disk space.
# 添加错误处理
    """
    disk = psutil.disk_usage('/')
    return {
        'total': disk.total / (1024 ** 3),  # Convert bytes to GB
        'used': disk.used / (1024 ** 3),  # Convert bytes to GB
        'free': disk.free / (1024 ** 3)  # Convert bytes to GB
    }


def get_network_usage():
    """Get the current network usage in bytes."""
    net_stats = psutil.net_io_counters()
    return {
        'sent': net_stats.bytes_sent,
        'received': net_stats.bytes_recv
    }


def main():
    """Main function to create the Gradio interface."""
# NOTE: 重要实现细节
    # Create a Gradio interface with two labels and four output boxes
# NOTE: 重要实现细节
    gr.Interface(
        fn=get_cpu_usage,
        inputs=[],
        outputs=[gr.outputs.Textbox(label="CPU Usage (%)")],
        title="System Performance Monitor"
    ).launch()
    gr.Interface(
        fn=get_memory_usage,
        inputs=[],
        outputs=[gr.outputs.Textbox(label="Memory Usage (GB)")],
        title="System Performance Monitor"
# 增强安全性
    ).launch()
    gr.Interface(
        fn=get_disk_usage,
        inputs=[],
        outputs=[
            gr.outputs.Textbox(label="Total Disk Space (GB)"),
# 增强安全性
            gr.outputs.Textbox(label="Used Disk Space (GB)"),
# TODO: 优化性能
            gr.outputs.Textbox(label="Free Disk Space (GB)")
        ],
        title="System Performance Monitor"
    ).launch()
    gr.Interface(
        fn=get_network_usage,
# NOTE: 重要实现细节
        inputs=[],
        outputs=[
            gr.outputs.Textbox(label="Network Sent (bytes)"),
            gr.outputs.Textbox(label="Network Received (bytes)")
        ],
# FIXME: 处理边界情况
        title="System Performance Monitor"
# NOTE: 重要实现细节
    ).launch()
# TODO: 优化性能

if __name__ == '__main__':
    main()