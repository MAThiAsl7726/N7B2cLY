# 代码生成时间: 2025-09-03 13:45:30
import os
import logging
from alembic.config import Config as AlembicConfig
from alembic import command
from gradio import Interface

# 设置日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

"""
数据库迁移工具 Gradio 界面
"""
class DatabaseMigrationTool:
    def __init__(self, alembic_config_path, template_path):
        """初始化数据库迁移工具
        :param alembic_config_path: Alembic 配置文件路径
        :param template_path: 模板文件路径
        """
        self.alembic_config_path = alembic_config_path
        self.template_path = template_path
        self.alembic_cfg = AlembicConfig()
        self.alembic_cfg.set_main_option("config", self.alembic_config_path)

    def upgrade_database(self):
        """执行数据库升级操作"""
        try:
            command.upgrade(self.alembic_cfg, "head")
            return "Database upgraded successfully."
        except Exception as e:
            logger.error("Failed to upgrade database: %s", str(e))
            return f"Error upgrading database: {str(e)}"

    def downgrade_database(self):
        """执行数据库降级操作"""
        try:
            command.downgrade(self.alembic_cfg, "-1")
            return "Database downgraded successfully."
        except Exception as e:
            logger.error("Failed to downgrade database: %s", str(e))
            return f"Error downgrading database: {str(e)}"

    def run_migration_tool(self):
        """运行数据库迁移工具"""
        # 创建 Gradio 界面
        interface = Interface(
            fn=self.upgrade_database, 
            inputs=[], 
            outputs="text", 
            examples=[], 
            title="Database Migration Tool", 
            description="A tool to upgrade and downgrade your database using Alembic."
        )
        interface.launch()

if __name__ == "__main__":
    # 指定 Alembic 配置文件路径和模板文件路径
    alembic_config_path = "alembic.ini"
    template_path = "env.py"

    # 创建数据库迁移工具实例
    db_migration_tool = DatabaseMigrationTool(alembic_config_path, template_path)

    # 运行数据库迁移工具
    db_migration_tool.run_migration_tool()
