# 代码生成时间: 2025-08-05 04:10:22
import gradio as gr
def scrape_content(url):
    """
    Fetches content from a given URL and returns it as a string.
    Includes error handling for network issues or invalid URLs.
    
    Args:
        url (str): The URL to scrape content from.
    
    Returns:
        str: The content of the webpage or an error message.
    """
    try:
        import requests
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"OOps: Something Else: {err}"
    
# Create a Gradio interface
iface = gr.Interface(
    fn=scrape_content, 
    inputs=gr.Textbox(label="Enter a URL"), 
    outputs="text", 
    title="Web Content Scraper",
    description="A tool to scrape content from any webpage."
)

iface.launch()