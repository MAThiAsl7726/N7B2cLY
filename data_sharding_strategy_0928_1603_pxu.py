# 代码生成时间: 2025-09-28 16:03:17
import numpy as np
from typing import List
import gradio as gr
def generate_data(size: int, num_shards: int) -> List[np.ndarray]:
    """Generates synthetic data to be sharded.
    
    Args:
        size (int): Total number of data points to generate.
        num_shards (int): Number of shards to split the data into.
    
    Returns:
        List[np.ndarray]: A list of numpy arrays, each representing a shard.
    """
    data = np.random.rand(size)
    shard_size = size // num_shards
    shards = [data[i * shard_size:(i + 1) * shard_size] for i in range(num_shards)]
    return shards

def validate_shard_size(num_shards: int, size: int) -> bool:
    """Validates if the shard size is appropriate for the given data size.
    
    Args:
        num_shards (int): Number of shards.
        size (int): Total number of data points.
    
    Returns:
        bool: True if shard size is valid, False otherwise.
    """
    if num_shards <= 0:
        raise ValueError("Number of shards must be greater than 0.")
    if size % num_shards != 0:
        print("Warning: Data size is not evenly divisible by the number of shards.")
    return True

def main():
    with gr.Blocks() as demo:
        gr.Markdown("# Data Sharding Strategy")
        gr.Markdown("Generate splits of data based on shards.")
        size = gr.Slider(minimum=100, maximum=10000, step=100, default=1000, label="Data Size")
        num_shards = gr.Slider(minimum=1, maximum=100, step=1, default=5, label="Number of Shards")
        generate_button = gr.Button("Generate Shards")
        shards_output = gr.Dataframe()
        
        def update_shards(data_size: int, shard_count: int):
            try:
                validate_shard_size(shard_count, data_size)
                shards = generate_data(data_size, shard_count)
                shards_df = [shards[i].flatten() for i in range(shard_count)]
                return shards_df
            except Exception as e:
                return [[str(e)]]
        
        generate_button.click(update_shards, inputs=[size, num_shards], outputs=shards_output)
        demo.launch()

if __name__ == "__main__":
    main()