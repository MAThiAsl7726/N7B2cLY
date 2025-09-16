# 代码生成时间: 2025-09-16 16:29:07
import gradio as gr
import requests
from bs4 import BeautifulSoup
import re

"""
A simple web content scraper using Python and Gradio framework.
"""

def scrape_website(url):
    """
    Fetch and scrape content from a website.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        str: The scraped content from the website.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract the text content
            content = soup.get_text()
            # Remove unnecessary whitespace and newline characters
            content = re.sub(r'\s+', ' ', content).strip()
            return content
        else:
            return "Failed to retrieve content. Status code: {}".format(response.status_code)
    except requests.RequestException as e:
        return "An error occurred while fetching the webpage: {}".format(e)

# Create a Gradio interface for the scraper
iface = gr.Interface(
    fn=scrape_website,
    inputs=gr.Textbox(label="Website URL"),
    outputs="text",
    title="Web Content Scraper",
    description="A simple tool to scrape content from websites."
)

# Launch the interface
iface.launch(share=True)