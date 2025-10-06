# 代码生成时间: 2025-10-06 21:00:54
import gr
from gr import *
from datetime import datetime
import random

"""
Health Monitor Service

This program simulates a health monitoring device using the Gradio framework.
It takes user input and displays the current health status based on the input data.
"""

def get_health_status(heart_rate, blood_pressure, blood_sugar):
    """
    Calculate the health status based on the input data.

    Args:
    heart_rate (int): Heart rate in beats per minute.
    blood_pressure (float): Blood pressure in mmHg.
    blood_sugar (float): Blood sugar level in mg/dL.

    Returns:
    str: Health status.
    """
    if heart_rate < 60 or heart_rate > 100:
        return "Heart rate is outside the normal range."
    elif blood_pressure < 90 or blood_pressure > 120:
        return "Blood pressure is outside the normal range."
    elif blood_sugar < 70 or blood_sugar > 140:
        return "Blood sugar level is outside the normal range."
    else:
        return "Your health status is good."

# Create a Gradio interface
iface = gr.Interface(
    fn=get_health_status,
    inputs=[
        gr.Slider(minimum=30, maximum=150, label="Heart Rate (BPM)"),
        gr.Slider(minimum=80, maximum=160, label="Blood Pressure (mmHg)"),
        gr.Slider(minimum=50, maximum=200, label="Blood Sugar (mg/dL)")
    ],
    outputs="text"
)

# Start the Gradio server
iface.launch(share=True)