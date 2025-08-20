# 代码生成时间: 2025-08-20 15:12:52
import psutil
from grADIO import Interface

"""
A simple GrADIO interface for analyzing memory usage.

Features:
- Displays current memory usage as a percentage of total memory.
- Provides a simple and clear interface for users.
"""

# Define a function to get memory usage
def get_memory_usage():
    try:
        # Get system memory usage stats
        mem = psutil.virtual_memory()
        # Calculate memory usage in percentage
        usage = mem.percent
        return f"Memory Usage: {usage}%"
    except Exception as e:
        # Handle potential errors
        return f"Error fetching memory usage: {e}"

# Create a GrADIO interface
iface = Interface(fn=get_memory_usage, inputs=[], outputs="text",
                  title="Memory Usage Analyzer", description="Analyze your system's memory usage.")

# Launch the interface
iface.launch()