import os
import time

import pytest

if __name__ == '__main__':
    try:
        print("开始执行脚本")
        pytest.main()
        time.sleep(3)
        os.system("copy environment.properties temps\environment.properties")
        print("脚本执行完成")
    except Exception as e:
        print("脚本批量执行失败！", e)

    try:
        print("开始执行报告生成")
        os.system('allure generate ./temps -o ./reports --clean')
        print("报告生成完毕")
        # os.system("allure open reports")
    except Exception as e:
        print("报告生成失败，请重新执行", e)