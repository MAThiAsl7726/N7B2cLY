# 代码生成时间: 2025-10-14 03:18:25
import gr

"""
健康风险评估程序

该程序使用GRADIO框架创建一个简单的网页界面，用户可以通过输入他们的年龄、性别、身高（厘米）、体重（公斤）来计算健康风险指数。
"""

# 定义健康风险评估函数
def health_risk_assessment(age, gender, height, weight):
    """根据用户提供的年龄、性别、身高和体重计算健康风险指数。

    参数:
    age (int): 用户年龄
    gender (str): 用户性别，'male' 或 'female'
    height (float): 用户身高（厘米）
    weight (float): 用户体重（公斤）

    返回:
    float: 健康风险指数

    异常:
    ValueError: 如果输入参数无效或不完整
    """
    if age < 0 or height <= 0 or weight <= 0:
        raise ValueError("年龄、身高和体重必须为正数")
    if gender not in ['male', 'female']:
        raise ValueError("性别必须是'male'或'female'")

    # BMI计算
    bmi = weight / (height / 100) ** 2

    # 健康风险指数计算（示例，实际计算方法需根据具体问题调整）
    risk_index = 1 + (bmi - 18.5) * 0.1 * (age - 30)

    return risk_index

# 创建GRADIO界面
def create_gradio_interface():
    """创建GRADIO界面，允许用户输入参数并显示健康风险评估结果。
    """
    demo = gr.Interface(
        fn=health_risk_assessment,
        inputs=[
            gr.Slider(0, 100, label="年龄"),
            gr.Radio(["male", "female"], label="性别"),
            gr.Slider(100, 250, label="身高（厘米）"),
            gr.Slider(30, 150, label="体重（公斤）"),
        ],
        outputs="text",
        title="健康风险评估",
        description="输入您的年龄、性别、身高和体重，我们将为您评估健康风险指数。"
    )
    demo.launch()

if __name__ == "__main__":
    create_gradio_interface()