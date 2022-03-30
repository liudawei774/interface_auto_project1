import pytest


class TestApi:


    # @pytest.mark.parametrize('args',['baili','ds'])
    # def test_api1(self,args):
    #     print(args)

    @pytest.mark.parametrize('name,age',[['bail12i','ds'],['xin333gyao','123']])
    def test_api2(self,name,age):
        print(f'{name}今年{age}岁')

if __name__ == '__main__':
    pytest.main(['-vs','test_shop.py'])
