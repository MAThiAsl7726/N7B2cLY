# 代码生成时间: 2025-08-20 09:13:29
import gradio as gr
def add_item(item_name, quantity):
    """Add a new item to the inventory."""
    if quantity <= 0:
        return f"Error: Quantity must be greater than 0 for {item_name}."
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    return f"Added {quantity} {item_name}(s) to inventory."

def remove_item(item_name, quantity):
    """Remove an item from the inventory."""
    if item_name not in inventory:
        return f"Error: Item {item_name} not found in inventory."
    if quantity <= 0:
        return f"Error: Quantity must be greater than 0 for {item_name}."
    if quantity > inventory[item_name]:
        return f"Error: Insufficient quantity of {item_name} in inventory."
    inventory[item_name] -= quantity
    return f"Removed {quantity} {item_name}(s) from inventory."

def get_inventory():
    """Return the current inventory."""
    return inventory
def reset_inventory():
    """Reset the inventory to an empty state."