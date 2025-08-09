# 代码生成时间: 2025-08-10 06:10:22
import os
import shutil
def organize_folder_structure(source_folder, target_folder, file_extension):
    """
    Function to organize files in a folder based on their extension.
    It moves files from the source folder to the target folder while creating
    subfolders for each file extension.
    """
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"Source folder {source_folder} does not exist.")
    
    # Check if the target folder exists, create if not
    os.makedirs(target_folder, exist_ok=True)
    
    for file_name in os.listdir(source_folder):
        # Get the file path
        file_path = os.path.join(source_folder, file_name)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension and create the target path
        _, ext = os.path.splitext(file_name)
        if ext == file_extension:
            target_path = os.path.join(target_folder, ext[1:])
            os.makedirs(target_path, exist_ok=True)
            
            # Move the file to the target path
            shutil.move(file_path, os.path.join(target_path, file_name))
            print(f"Moved {file_path} to {os.path.join(target_path, file_name)}")
        else:
            print(f"Skipped {file_path} as it does not match the required extension.")
        
# Create a Gradio interface
import gr

def main():
    # Define the input elements
    with gr.Blocks() as "Folder Structure Organizer":
        source_folder_input = gr.Textbox(label="Source Folder Path")
        target_folder_input = gr.Textbox(label="Target Folder Path")
        file_extension_input = gr.Textbox(label="File Extension (e.g., 'txt')")
        
        organize_button = gr.Button("Organize")
        
        # Define the output element
        output_text = gr.Textbox(label="Output", visible=False)
        
        # Define the callback function
        def organize_callback(source_folder, target_folder, file_extension):
            try:
                organize_folder_structure(source_folder, target_folder, file_extension)
                output_text.update(value="Files have been organized successfully.", visible=True)
            except Exception as e:
                output_text.update(value=str(e), visible=True)
                
        organize_button.click(organize_callback, inputs=[source_folder_input, target_folder_input, file_extension_input], outputs=[output_text])
        
    # Launch the interface
    launch()

def launch():
    """
    Function to launch the Gradio interface.
    """
    import gr
    gr.launch()

if __name__ == "__main__":
    main()