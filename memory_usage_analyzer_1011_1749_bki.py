# 代码生成时间: 2025-10-11 17:49:46
import psutil
import gradio as gr

"""
Memory Usage Analyzer using Python and Gradio.
This program provides a simple interface to analyze and visualize
the memory usage of the system.
"""

def analyze_memory_usage():
    """
    Analyzes the system memory usage and returns statistics.
    """
    try:
        # Get system memory usage stats
        mem = psutil.virtual_memory()
        
        # Create a dictionary to store memory usage data
        memory_stats = {
            'total': mem.total / (1024 ** 3),  # GB
            'available': mem.available / (1024 ** 3),  # GB
            'used': mem.used / (1024 ** 3),  # GB
            'free': mem.free / (1024 ** 3),  # GB
            'percent': mem.percent  # Percentage
        }
        return memory_stats
    except Exception as e:
        # Handle any exceptions that occur during memory analysis
        return {"error": str(e)}

def visualize_memory_usage(mem_stats):
    """
    Visualizes the memory usage stats using Gradio interface.
    """
    # Create a Gradio interface
    with gr.Blocks() as demo:
        gr.Markdown("What is the system's memory usage like?")
        gr.Markdown("### Memory Usage Statistics")
        for key, value in mem_stats.items():
            gr.Text(f"{key.capitalize()}: {value}")
    
    return demo

# Create a Gradio interface to analyze and visualize memory usage
if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Markdown("# System Memory Usage Analyzer")
        gr.Markdown("Use this tool to analyze the system's memory usage.")
        analyze_button = gr.Button("Analyze Memory Usage")
        mem_stats_output = gr.Textbox()
        analyze_button.click(fn=analyze_memory_usage, outputs=mem_stats_output)
        gr.Row([analyze_button, mem_stats_output])
    demo.launch()