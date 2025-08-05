# 代码生成时间: 2025-08-05 13:38:49
import gradio as gr
def get_product_info(product_id):
    """
    根据产品ID获取产品信息
    参数:
    product_id (str): 产品ID
    返回:
    dict: 包含产品名称和库存数量的字典
    """
    try:
        product_info = inventory[product_id]
        return {"name": product_info["name"], "stock": product_info["stock"]}
    except KeyError:
        return {"error": "Product not found"}

def update_stock(product_id, quantity):
    """
    更新库存数量
    参数:
    product_id (str): 产品ID
    quantity (int): 更新的数量
    返回:
    str: 更新结果
    """
    try:
        if inventory[product_id]["stock"] + quantity < 0:
            return "Not enough stock"
        inventory[product_id]["stock"] += quantity
        return "Stock updated successfully"
    except KeyError:
        return "Product not found"

def add_product(product_id, name, quantity):
    """
    添加新产品
    参数:
    product_id (str): 产品ID
    name (str): 产品名称
    quantity (int): 初始库存数量
    返回:
    str: 添加结果
    """
    if product_id in inventory:
        return "Product already exists"
    inventory[product_id] = {"name": name, "stock": quantity}
    return "Product added successfully"

# 初始化库存字典
inventory = {}
# 添加示例产品
inventory["P001"] = {"name": "Product 1", "stock": 100}
inventory["P002"] = {"name": "Product 2", "stock": 50}

# 创建Gradio界面
demo = gr.Interface(
    fn=get_product_info,
    inputs=[gr.Textbox(label="Product ID")],
    outputs=["json"],
    title="Inventory Management"
)

# 添加更新库存的界面
update_demo = gr.Interface(
    fn=update_stock,
    inputs=[gr.Textbox(label="Product ID"), gr.Number(label="Quantity", default=0)],
    outputs=["text"],
    title="Update Stock"
)

# 添加添加产品的界面
add_product_demo = gr.Interface(
    fn=add_product,
    inputs=[gr.Textbox(label="Product ID"), gr.Textbox(label="Product Name"), gr.Number(label="Quantity", default=0)],
    outputs=["text"],
    title="Add Product"
)

# 运行Gradio应用
if __name__ == __main__":
    demo.launch()
    update_demo.launch()
    add_product_demo.launch()
