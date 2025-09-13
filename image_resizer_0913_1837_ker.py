# 代码生成时间: 2025-09-13 18:37:13
import gradio as gr
def resize_images(input_images, desired_width, desired_height):
    # This function resizes the input images to the desired dimensions
    resized_images = []
    for img in input_images:
        try:
            from PIL import Image
            img = Image.open(img)
            # Resize the image
            img = img.resize((desired_width, desired_height), Image.ANTIALIAS)
            # Save the resized image in a memory buffer
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG")
            buffer.seek(0)
            resized_images.append(buffer)
        except Exception as e:  # Handle exceptions, e.g., file not found, wrong file format
            print(f"Error resizing image: {e}
")
    return resized_images

def main():
    # Set up Gradio interface
    demo = gr.Interface(
        resize_images,
        inputs=[
            gr.inputs.ImageMultiple(label="Select multiple images for resizing"),
            gr.inputs.Slider(1, 2000, label="Width"),
            gr.inputs.Slider(1, 2000, label="Height")
        ],
        outputs=gr.outputs.ImageMultiple(label="Resized images")
    )
    demo.launch()

if __name__ == "__main__":
    main()
