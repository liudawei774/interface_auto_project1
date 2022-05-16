import pytest

from common.yaml_util import yamlUtil


class TestApi:


    # @pytest.mark.parametrize('args',['baili','ds'])
    # def test_api1(self,args):
    #     print(args)
    @pytest.mark.parametrize("except_result, except_code, except_msg",
                             yamlUtil().read_yaml_nf('testcases/testcase', 'test.yaml')["test_get_all_user_info"])
    def test_api2(self,except_result, except_code, except_msg):
        print(except_result, except_code, except_msg)
        # print(data['CreateDevice'])

if __name__ == '__main__':
    # print(yamlUtil().read_yaml_nf('testcases/testcase', 'test.yaml'))
    pytest.main(['-q -s','test_api.py'])
