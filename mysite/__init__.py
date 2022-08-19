# 这将确保应用程序总是导入
# Django启动，以便shared_task装饰器使用这个应用程序。
from .celery import app as celery_app

__all__ = ('celery_app',)

