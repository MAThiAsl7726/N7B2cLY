# 代码生成时间: 2025-08-06 17:41:28
作者：[你的名字]
日期：2023-12-07
*/

import gradio as gr

# 定义库存数据结构
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

# 初始库存数据
inventory = [
    InventoryItem("Apple", 100),
    InventoryItem("Banana", 150),
    InventoryItem("Cherry", 200)
]

# 显示库存信息
def display_inventory():
    # 将库存数据转换为字典列表
    inventory_list = [
        {
            "name": item.name,
            "quantity": item.quantity
        } for item in inventory
    ]
    return inventory_list

# 添加库存
def add_inventory(item_name, quantity):
    # 检查库存中是否已存在该商品
    for item in inventory:
        if item.name == item_name:
            return f"Error: {item_name} already exists in inventory"
    # 添加新商品到库存
    inventory.append(InventoryItem(item_name, quantity))
    return f"{item_name} added to inventory"

# 删除库存
def remove_inventory(item_name):
    # 检查库存中是否存在该商品
    for i, item in enumerate(inventory):
        if item.name == item_name:
            del inventory[i]
            return f"{item_name} removed from inventory"
    return f"Error: {item_name} not found in inventory"

# 更新库存数量
def update_inventory(item_name, quantity):
    # 检查库存中是否存在该商品
    for item in inventory:
        if item.name == item_name:
            item.quantity = quantity
            return f"{item_name} quantity updated to {quantity}"
    return f"Error: {item_name} not found in inventory"

# 创建GUI界面
iface = gr.Interface(
    fn=display_inventory,
    inputs=[],
    outputs="json",
    title="Inventory Management System",
    description="Manage your inventory with this simple system"
)

# 添加按钮和输入框
iface.add_button(
    label="Add Inventory",
    inputs=["text", "number"],
    outputs="text",
    value=["", 0],
    elem_id="add_button"
)
iface.add_item("add_button", add_inventory)

iface.add_button(
    label="Remove Inventory",
    inputs=["text"],
    outputs="text",
    value="",
    elem_id="remove_button"
)
iface.add_item("remove_button", remove_inventory)

iface.add_button(
    label="Update Inventory",
    inputs=["text", "number"],
    outputs="text",
    value=["", 0],
    elem_id="update_button"
)
iface.add_item("update_button", update_inventory)

# 启动应用
iface.launch()