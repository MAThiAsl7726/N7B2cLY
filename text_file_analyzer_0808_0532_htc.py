# 代码生成时间: 2025-08-08 05:32:35
import gradio as gr
def analyze_text_file(file_path):    """Analyze the provided text file and return the count of characters, words, and lines."""    try:        with open(file_path, 'r', encoding='utf-8') as file:            content = file.read()            # Count characters (excluding spaces)            char_count = len(''.join(content.split()))            # Count words            words = content.split()            word_count = len(words)            # Count lines            line_count = content.count('
')            return {
                'characters': char_count,
                'words': word_count,
                'lines': line_count
            }    except FileNotFoundError:        return {'error': 'File not found'}    except Exception as e:        return {'error': str(e)}

# Define the Gradio interfaceiface = gr.Interface(
    fn=analyze_text_file,
    inputs=gr.File(label='Upload text file'),
    outputs=gr.JSON(label='Analysis results'),
    title='Text File Content Analyzer',
    description='Upload a text file to analyze its content.',
    examples=[['example.txt']],
)

# Run the interfaceiface.launch()