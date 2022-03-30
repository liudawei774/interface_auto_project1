import yaml
from common.path_util import Path


class yamlUtil:

    def read_yaml(self, filename):
        with open((Path().get_config_path(filename)), mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

        # 写入yaml文件

    def write_yaml(self, filename, data):
        with open((Path().get_config_path(filename)), mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

        # 清除文件

    def clear_yaml(self, filename):
        with open((Path().get_config_path(filename)), mode='w', encoding='utf-8') as f:
            f.truncate()

        # def merge_config(config, args):
        #     for key_1 in config.keys():
        #         if (isinstance(config[key_1], dict)):
        #             for key_2 in config[key_1].keys():
        #                 if (key_2) in dir(args):
        #                     config[key_1][key_2] = getattr(args, key_2)
        #     return config

    # 读取非config目录yaml文件
    def read_yaml_nf(self, dirname, filename):
        with open(Path().get_real_path(dirname, filename), mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    def write_yaml_nf(self, dirname, filename, data):
        with open((Path().get_real_path(dirname, filename)), mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)
