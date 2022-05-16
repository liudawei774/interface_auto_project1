import os
import time

import pytest

from common import Shell

if __name__ == '__main__':
    try:
        print("开始执行脚本")
        pytest.main()
        time.sleep(3)
        os.system("copy environment.properties temps\environment.properties")
        # pytest.main(['E:\\project\\Xiaoniu_Api_Rili\\test_case', '--alluredir',
        # 'E:\\project\\Xiaoniu_Api_Rili\\report\\reportallure'])
        # logger.info("脚本执行完成")
        print("脚本执行完成")
    except Exception as e:
        print("脚本批量执行失败！", e)

    try:
        print("开始执行报告生成")
        os.system('allure generate ./temps -o ./reports --clean')
        print("报告生成完毕")
        os.system("allure open reports")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        # logger.error("报告生成失败，请重新执行", e)
        # log.error('执行用例失败，请检查环境配置')
        raise