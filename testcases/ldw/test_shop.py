import os

import allure
import pytest

from common.request_util import requestsUtil
from common.update_allure import JsonAlter
from common.yaml_util import yamlUtil

from common.logger_handler import logger

class Test_Mullogin():

    @pytest.mark.smoke
    @pytest.mark.parametrize('caseinfo', yamlUtil().read_yaml_nf('testcases/testcase', 'yhdl.yml'))
    def test_001_yhdl(self, caseinfo):
        # print(caseinfo['name'])
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        userinfo = caseinfo['request']['data']
        # 发送登录请求并获取响应
        response = requestsUtil().send_request(method, url, userinfo)
        logger.info('*' * 88)
        logger.info('接口用例名称：{}'.format(caseinfo['name']))
        logger.info('接口请求方法：{}'.format(method))
        logger.info('接口url地址：{}'.format(url))
        logger.info('接口测试数据：{}'.format(userinfo))
        try:
            # 断言：预期结果与实际结果对比
            assert '登录成功' == response['msg']
            logger.info('响应结果：{}'.format(response))
            result = 'Pass'
        except AssertionError as e:
            logger.error('用例执行失败：{}'.format(e))
            result = 'Fail'
            raise e

    @pytest.mark.parametrize('caseinfo', yamlUtil().read_yaml_nf('testcases/testcase', 'tjmbwtda.yml'))
    def test_002_yhzc(self, caseinfo):
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        # 正确的用户注册数据
        userinfo = caseinfo['request']['data']
        # 发送注册请求并获取响应
        response = requestsUtil().send_request(method, url, userinfo)
        logger.info('*' * 88)
        logger.info('接口用例名称：{}'.format(caseinfo['name']))
        logger.info('接口请求方法：{}'.format(method))
        logger.info('接口url地址：{}'.format(url))
        logger.info('接口测试数据：{}'.format(userinfo))
        try:
            # 断言：预期结果与实际结果对比
            assert '注册成功' == response['msg']
            logger.info('响应结果：{}'.format(response))
            result = 'Pass'
        except AssertionError as e:
            logger.error('用例执行失败：{}'.format(e))
            result = 'Fail'
            raise e

    @pytest.mark.parametrize('caseinfo', yamlUtil().read_yaml_nf('testcases/testcase', 'wjmi.yml'))
    def test_003_wjmi(self,caseinfo):
        method=caseinfo['request']['method']
        url = caseinfo['request']['url']
        # 忘记密码对应的用户
        userinfo = caseinfo['request']['data']
        # 发送忘记密码请求并获取响应
        response = requestsUtil().send_request(method, url, data=userinfo)
        logger.info('*' * 88)
        logger.info('接口用例名称：{}'.format(caseinfo['name']))
        logger.info('接口请求方法：{}'.format(method))
        logger.info('接口url地址：{}'.format(url))
        logger.info('接口测试数据：{}'.format(userinfo))

    @allure.description("测试http://calapi.51jirili.com/dream/categoryList接口")
    @allure.testcase("http://calapi.51jirili.com/dream/categoryList", "测试用例地址👇")
    @pytest.mark.test
    def test_004_tjmbwtda(self, conn_connert):
        url = "http://localhost:8080/jwshoplogin/user/forget_check_answer.do"
        # 密保问题答案
        userinfo = {"username": "刘婷1",
                    "question": "喜欢吃的水果",
                    "answer": "香蕉"
                    }
        # 发送密保问题答案并获取响应
        # response = requests.session().post(url, data=userinfo)

        response = requestsUtil().send_request('post', url, userinfo)
        print(response)

        # print(json.loads(response))
        # 把返回的json字典中的data存到yaml文件里
        yamlUtil().write_yaml_nt('testcases/testcase', {'data': response['data']})
        # assert 'data' in response.json()
    @allure.description("测试http://calapi.51jirili.com/dream/categoryList接口")
    @allure.testcase("http://www.baidu.com", "测试用例地址👇")
    @pytest.mark.smoke
    def test_005_hdwtxgmm(self):
        url = "http://localhost:8080/jwshoplogin/user/forget_reset_password.do"
        forgettoken = yamlUtil().read_yaml_nf('testcases/testcase','hdwtxgmm.yml')['request']['data']['forgetToken']
        userinfo = {"username": "刘婷1",
                    "passwordNew": "111111",
                    "forgetToken": forgettoken
                    }
        # yamlUtil().write_yaml('extract', userinfo)
        # 发送忘记密码请求并获取响应
        response = requestsUtil().send_request('post', url, data=userinfo)
        print(response)