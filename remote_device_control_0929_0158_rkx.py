# 代码生成时间: 2025-09-29 01:58:23
import gradio as gr
def control_device(action):
    """
    控制设备执行不同动作。
    参数:
    action (str): 要执行的动作，例如'on'、'off'、'reset'等。
    返回值:
    str: 表示设备状态的字符串。
    """
    try:
        # 模拟设备控制逻辑
        if action == 'on':
            return '设备已开启'
        elif action == 'off':
            return '设备已关闭'
        elif action == 'reset':
            return '设备已重置'
        else:
            return '未知动作'
    except Exception as e:
        return f'发生错误: {e}'

# 创建Gradio界面
iface = gr.Interface(
    fn=control_device,
    inputs=gr.Textbox(label='请输入动作'),
    outputs='text',
    title='设备远程控制',
    description='通过输入指令来控制设备的开启、关闭和重置。'
)

# 运行Gradio界面
iface.launch()