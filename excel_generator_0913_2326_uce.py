# 代码生成时间: 2025-09-13 23:26:48
import gradio as gr
def create_excel(title, data):    """
    Generate an Excel file with the given title and data.
    
    Parameters:
    title (str): The title of the Excel file.
    data (list of lists): A 2D list containing the data to be written into the Excel file.
    
    Returns:
    bytes: A bytes object representing the Excel file.
    """    try:        import xlsxwriter        import io        from openpyxl import Workbook
        # Create a new Excel workbook
        wb = Workbook()        sheet = wb.active
        sheet.title = title
        
        # Write data to the Excel file
        for row in data:            sheet.append(row)        
        
        # Save the workbook to a bytes buffer
        buf = io.BytesIO()        wb.save(buf)        
        
        # Return the bytes buffer
        return buf.getvalue()    except Exception as e:        print(f"An error occurred: {e}")        
        return None

# Create a Gradio interface
iface = gr.Interface(    create_excel,
    inputs=["text", "json"],
    outputs="file",
    title="Excel Generator",
    description="Generate an Excel file from text and JSON data."
)

# Launch the interface
iface.launch()