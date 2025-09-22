# 代码生成时间: 2025-09-23 01:00:31
import zipfile
import os
import gr
from gr import Gr

# 定义一个函数来解压文件
def unzip_file(file_path, output_dir):
    # 检查输出目录是否存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # 使用zipfile模块解压文件
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        return f"Files extracted to {output_dir}"
    except zipfile.BadZipFile:
        return "Error: The file is not a zip file or is corrupted."
    except Exception as e:
        return f"An error occurred: {e}"

# 定义一个函数来获取文件并解压
def process_upload(file):
    # 指定解压文件的输出目录
    output_dir = './extracted_files/'
    return unzip_file(file.name, output_dir)

# 初始化Gr库
iface = Gr()

# 添加文件上传组件
iface.add_file('Upload zip file')

# 添加文本输出组件，用于显示解压结果
iface.add_text('Result')

# 定义回调函数，将上传的文件传递给process_upload函数
def upload_callback(file):
    result = process_upload(file)
    iface.outputs[0].update(result)

# 将文件上传组件与回调函数关联
iface.add_callback(upload_callback, iface.inputs[0], iface.outputs[0])

# 启动GUI
iface.launch()