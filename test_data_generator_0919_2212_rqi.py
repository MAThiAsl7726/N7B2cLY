# 代码生成时间: 2025-09-19 22:12:46
import gradio as gr
def generate_test_data(num_samples, seed):    """
    Function to generate random test data.
    Args:
    num_samples (int): Number of samples to generate.
    seed (int): Seed for the random number generator for reproducibility.
    Returns:
    list: A list of randomly generated test data.
    """    
    import random
    import numpy as np
    
    # Set the seed for reproducibility
    np.random.seed(seed)
    random.seed(seed)
    
    # Generate random test data
    test_data = []
    for _ in range(num_samples):
        data_point = {
            "id": np.random.randint(1, 1000),
            "feature1": np.random.normal(0, 1),
            "feature2": np.random.randint(0, 100),
            "label": np.random.choice(["class1", "class2"])
        }
        test_data.append(data_point)
    
    return test_data

# Create a Gradio interface
iface = gr.Interface(
    fn=generate_test_data,
    inputs=[
        gr.Slider(label="Number of samples", minimum=1, maximum=100, step=1, default=10),
        gr.Slider(label="Random seed", minimum=0, maximum=10000, step=1, default=42)
    ],
    outputs=["json"],
    title="Test Data Generator",
    description="Generate random test data using Gradio."
)

# Run the interface
iface.launch()