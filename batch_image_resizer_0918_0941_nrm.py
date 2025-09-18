# 代码生成时间: 2025-09-18 09:41:09
import os
from PIL import Image
import gr
from gr import Interface

"""
Batch Image Resizer

This program utilizes the GrAPI framework to create a user interface for batch resizing images.
Users can upload multiple images, select the desired output size, and download the resized images.

Attributes:
    - None

Methods:
    resize_images: Resizes the images to the specified dimensions.

Example:
    >>> batch_resizer = BatchImageResizer()
    >>> batch_resizer.run()

Note:
    This program assumes that the images are in a compatible format for the PIL library.
"""

class BatchImageResizer:
    def __init__(self):
        """Initializes the BatchImageResizer instance."""
        self.interface = Interface(fn=self.resize_images, inputs=["image", "number"],
                                  outputs="image")

    def resize_images(self, images, size):
        """Resizes the images to the specified dimensions.

        Args:
            images (list): A list of PIL Image objects.
            size (tuple): The desired output size (width, height).

        Returns:
            list: A list of resized PIL Image objects.
        """
        resized_images = []
        for image in images:
            try:
                # Resize the image to the specified size
                resized_image = image.resize(size, Image.ANTIALIAS)
                resized_images.append(resized_image)
            except Exception as e:
                # Handle any errors that occur during resizing
                print(f"Error resizing image: {e}")
        return resized_images

    def run(self):
        """Runs the GrAPI interface."""
        self.interface.launch()

if __name__ == "__main__":
    # Create an instance of BatchImageResizer and run the GrAPI interface
    batch_resizer = BatchImageResizer()
    batch_resizer.run()