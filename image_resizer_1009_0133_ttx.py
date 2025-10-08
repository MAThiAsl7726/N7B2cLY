# 代码生成时间: 2025-10-09 01:33:23
import gradio as gr
from PIL import Image
import os

"""
Image Resizer: A program that allows users to batch resize images using Gradio framework.
"""

def resize_images(input_images, new_size):
    """
    Resizes a list of images to a specified size.
    
    Args:
    input_images (list): List of input image file paths.
    new_size (tuple): The new size (width, height) for the images.
    
    Returns:
    list: List of resized images as file paths.
    """
    resized_images = []
    for image_path in input_images:
        try:
            # Open an image file
            with Image.open(image_path) as img:
                # Resize the image
                img_resized = img.resize(new_size)
                # Save the resized image in the same directory with '_resized' appended to the filename
                filename, file_extension = os.path.splitext(image_path)
                resized_image_path = f"{filename}_resized{file_extension}"
                img_resized.save(resized_image_path)
                # Append the resized image path to the list
                resized_images.append(resized_image_path)
        except Exception as e:
            print(f"Error resizing image {image_path}: {e}")
    return resized_images

# Define Gradio interface
if __name__ == "__main__":
    # Create a Gradio interface with two inputs: a list of images and a new size
    gr_interface = gr.Interface(
        func=resize_images,
        inputs=[
            gr.File(label="Select images"),
            gr.Slider(minimum=100, maximum=1000, step=10, default=(300, 300), label="New size (width, height)"),
        ],
        outputs="file",
        live=False,
    )
    # Launch the interface
    gr_interface.launch()