import os


class Path:
    def __init__(self):
        self.base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

    def get_base_path(self):
        return self.base_path

    # 获取文件的绝对路径
    # dirname :父目录  filename:文件名
    def get_real_path(self, dirname, filename):
        return os.path.join(self.base_path, dirname, filename)

    # 获取配置文件的绝对路径
    def get_config_path(self, filename):
        return os.path.join(self.base_path, 'config', filename)
