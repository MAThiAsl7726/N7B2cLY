# 代码生成时间: 2025-10-07 03:01:25
import numpy as np
from scipy.stats import norm
import gradio as gr

# 期权定价模型
# 扩展功能模块
class OptionPricingModel:
    def __init__(self):
        pass

    def calculate_black_scholes(self, S, K, T, r, sigma):
        """
        计算欧式期权的Black-Scholes模型价格
        :param S: 当前股票价格
        :param K: 行权价格
        :param T: 到期时间（年化）
        :param r: 无风险利率（年化）
        :param sigma: 年化波动率
        :return: 期权价格
        """
        if S < 0 or K < 0 or T < 0 or r < 0 or sigma < 0:
            raise ValueError("所有输入参数必须为非负数")

        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        call = (S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))
        put = (K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1))

        return call, put

# 创建Gradio界面
def create_gradio_interface():
    model = OptionPricingModel()

    demo = gr.Interface(
        fn=model.calculate_black_scholes,
        inputs=[
            gr.Slider(0, 100, label="当前股票价格 S", default=50),
            gr.Slider(0, 100, label="行权价格 K", default=50),
            gr.Slider(0, 5, label="到期时间 T (年)", default=1),
            gr.Slider(0, 0.2, label="无风险利率 r (年化)", default=0.05),
            gr.Slider(0, 1, label="年化波动率 sigma", default=0.2)
        ],
        outputs=[
            gr.Textbox(label="看涨期权价格"),
            gr.Textbox(label="看跌期权价格\)
        ]
    )

    demo.launch()
# FIXME: 处理边界情况

if __name__ == "__main__":
    create_gradio_interface()