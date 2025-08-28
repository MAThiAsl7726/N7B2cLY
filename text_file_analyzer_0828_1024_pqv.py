# 代码生成时间: 2025-08-28 10:24:13
import gradio as gr
def analyze_text(file):
    """
    Function to analyze text content from a file.
    
    Args:
        file (str): The content of the text file.
    
    Returns:
        dict: A dictionary containing the word count and sentence count.
    """
    try:
        # Split the file into sentences and words
        sentences = file.split('. ')
        words = file.split()
        
        # Count the sentences and words
        sentence_count = len(sentences)
        word_count = len(words)
        
        # Return the counts in a dictionary
        return {"Word Count": word_count, "Sentence Count": sentence_count}
    except Exception as e:
        # Handle any exceptions that occur during analysis
        return {"Error": str(e)}

# Create a Gradio interface
iface = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(label="Upload your text file"),
    outputs="json",
    title="Text File Content Analyzer",
    description="Analyze the content of your text files."
)

# Launch the interface
iface.launch()