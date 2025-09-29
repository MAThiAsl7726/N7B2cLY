# 代码生成时间: 2025-09-30 02:22:18
import gradio as gr
def assign_task(task_name, assignee_name):
    """
    This function assigns a task to a specified assignee.
    Args:
        task_name (str): The name of the task to be assigned.
        assignee_name (str): The name of the assignee to whom the task is assigned.
    Returns:
        str: A message indicating the task assignment status.
    """
    if not task_name or not assignee_name:
        return "Task name and assignee name are required."
    return f"Task '{task_name}' has been assigned to {assignee_name}."

# Create a Gradio interface
iface = gr.Interface(
    func=assign_task,
    inputs=[
        gr.Textbox(label="Task Name"),
        gr.Textbox(label="Assignee Name")
    ],
    outputs="text"
)

# Run the interface
iface.launch()