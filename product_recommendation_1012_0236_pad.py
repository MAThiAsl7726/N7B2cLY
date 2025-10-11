# 代码生成时间: 2025-10-12 02:36:24
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import grradio as gr

# 商品数据
products = pd.DataFrame(
    {
        "product_name": ["Apple iPhone 13", "Samsung Galaxy S22", "Google Pixel 6", "Apple MacBook Air", "Dell XPS 13"],
        "description": [
            "The latest iPhone with A15 Bionic chip and 5G support.",
            "The flagship phone from Samsung with Exynos 2200 and 5G.",
            "Google's flagship with Google Tensor and 5G.",
            "MacBook Air with M1 chip, 13.3" Retina display.",
            "Dell's flagship notebook with Intel i7, 13.3" display."
        ]
    }
)

# 使用TF-IDF对商品描述进行向量化
vectorizer = TfidfVectorizer(stop_words='english')
product_matrix = vectorizer.fit_transform(products["description"])

# 计算商品之间的相似度
def get_similar_products(product_name):
    """
    根据输入的商品名称返回相似商品的列表
    :param product_name: str, 输入的商品名称
    :return: list, 相似商品列表
    """
    try:
        product_index = products[products["product_name"] == product_name].index[0]
        product_vector = product_matrix[product_index]
        cosine_similarities = cosine_similarity(product_vector, product_matrix)
        similarity_scores = list(enumerate(cosine_similarities[0]))
        sorted_similarities = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]
        similar_products = [
            (products["product_name"][i], score) for i, score in sorted_similarities[:3]
        ]
        return similar_products
    except Exception as e:
        print(f"Error: {e}")
        return []

# GrADIO界面
def recommend_products(product_name):
    """
    根据输入的商品名称返回推荐商品的列表
    :param product_name: str, 输入的商品名称
    :return: list, 推荐商品列表
    """
    similar_products = get_similar_products(product_name)
    return [product[0] for product in similar_products]

# 创建GrADIO界面
iface = gr.Interface(
    fn=recommend_products,
    inputs=gr.Textbox(label="Enter Product Name"),
    outputs="text",
    title="Product Recommendation Engine",
    description="Enter a product name to get recommendations of similar products."
)
iface.launch()
