# 代码生成时间: 2025-10-12 23:14:58
import gradio as gr

class Achievement:
    """Class to represent an achievement with a name and description."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def unlock(self):
        """Method to simulate unlocking the achievement."""
        print(f"Achievement unlocked: {self.name}\
Description: {self.description}")

class AchievementSystem:
    """Class to manage a collection of achievements."""
    def __init__(self):
        self.achievements = {}

    def add_achievement(self, name, description):
        """Add a new achievement to the system."""
        if name in self.achievements:
            raise ValueError(f"Achievement '{name}' already exists.")
        self.achievements[name] = Achievement(name, description)

    def unlock_achievement(self, name):
        """Unlock an achievement by its name."""
        if name not in self.achievements:
            raise ValueError(f"Achievement '{name}' does not exist.")
        self.achievements[name].unlock()

    def list_achievements(self):
        """List all achievements in the system."""
        for name, achievement in self.achievements.items():
            print(f"{name} - {achievement.description}")

# Example achievements
ach_system = AchievementSystem()
ach_system.add_achievement("First Login", "You have logged in for the first time.")
ach_system.add_achievement("First Task", "You have completed your first task.")

# Gradio interface
def unlock_achievement(name):
    "