# 代码生成时间: 2025-08-09 18:04:55
import gradio as gr
import schedule
import threading
import time
from datetime import datetime

"""
Scheduled Task Scheduler using Python and Gradio framework.
This script creates a web interface to schedule and run tasks at specified times.
"""

# Define a function to execute the scheduled tasks
def run_scheduled_tasks():
    # Acquire the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Tasks executed at: {current_time}")

    # Here you can add the actual task to be executed
    # For demonstration, we'll just print a message
    print("This is a scheduled task.")

# Function to start the scheduler
def start_scheduler():
    try:
        # Schedule the task every minute. You can adjust the schedule according to your needs
        schedule.every(1).minute.do(run_scheduled_tasks)
        
        # Start the scheduler in a separate thread to avoid blocking the main thread
        threading.Thread(target=schedule.every(1).minute.do(run_scheduled_tasks), daemon=True).start()
    except Exception as e:
        print(f"An error occurred while starting the scheduler: {e}")

# Gradio interface to display the current time and status of the scheduler
iface = gr.Interface(
    fn=lambda: "Scheduler is running.",
    inputs=[],
    outputs="text",
    title="Scheduled Task Scheduler",
    description="A simple web interface to manage and monitor scheduled tasks."
)

# Start the scheduler
start_scheduler()

# Run the Gradio interface in a separate thread to avoid blocking
threading.Thread(target=iface.launch, daemon=True).start()

# Keep the main thread running to prevent the program from exiting
while True:
    time.sleep(1)