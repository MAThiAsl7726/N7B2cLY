# 代码生成时间: 2025-08-02 04:08:53
import re
import gr
from gr.inputs import File
from gr.outputs import Label

# Define a regex pattern for log entries
LOG_PATTERN = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(INFO|ERROR)\] (.*)$"

# Define a function to parse a log file
def parse_log_file(log_content):
    """Parses the log file content and extracts log entries."""
    lines = log_content.splitlines()
    parsed_entries = []
    for line in lines:
        match = re.match(LOG_PATTERN, line)
        if match:
            parsed_entries.append({
                "timestamp": match.group(1),
                "level": match.group(2),
                "message": match.group(3)
            })
    return parsed_entries

# Define a function to format the parsed log entries
def format_parsed_entries(entries):
    """Formats the parsed log entries into a readable string."""
    formatted_entries = []
    for entry in entries:
        formatted_entries.append(f"{entry['timestamp']} [{entry['level']}] {entry['message']}")
    return "
".join(formatted_entries)

# Create a Gradio interface
iface = gr.Interface(
    fn=parse_log_file,
    inputs=File(label="Upload log file"),
    outputs=Label(label="Parsed log entries"),
    title="Log File Parser",
    description="Upload a log file to parse its entries."
)

# Define error handling
iface.error = lambda error: f"An error occurred: {error}"

# Run the Gradio interface
iface.launch()
