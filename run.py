import os

import pytest

from common.update_allure import JsonAlter

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate temp -o reports --clean')

    w = JsonAlter()
    the_revised_dict = w.get_json_data('接口测试报告')
    w.write_json_data(the_revised_dict)
