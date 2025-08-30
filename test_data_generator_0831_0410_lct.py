# 代码生成时间: 2025-08-31 04:10:21
import gr
import random
import string

# 测试数据生成器类
class TestDataGenerator:
    def __init__(self, num_samples=100, length=10):
        """
        初始化测试数据生成器。
        :param num_samples: 生成样本的数量，默认为100。
        :param length: 生成字符串的长度，默认为10。
        """
        self.num_samples = num_samples
        self.length = length

    def generate_random_string(self):
        """
        生成指定长度的随机字符串。
        :return: 随机字符串。
        """
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(self.length))

    def generate_test_data(self):
        """
        生成测试数据。
        :return: 生成的测试数据列表。
        """
        try:
            test_data = [self.generate_random_string() for _ in range(self.num_samples)]
            return test_data
        except Exception as e:
            print(f"Error generating test data: {e}")
            return []

# 使用GRADIO创建一个简单的界面
def main():
    gen = TestDataGenerator()
    gr.Interface(
        fn=gen.generate_test_data,
        inputs=gr.inputs.Dropdown(num_samples=[10, 100, 1000], default=100, label="Number of samples"),
        outputs=gr.outputs.Textbox(label="Test Data"),
        description="Generate random test data"
    ).launch()

if __name__ == "__main__":
    main()