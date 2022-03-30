import requests


class requestsUtil:
    def __init__(self):
        """初始化session对象"""
        self.session=requests.Session()
    def send_request(self,method,url,data=None,json=None,**kwargs):
        if method=='get':
            response=self.session.request('get',url,params=data)
        else:
            response=self.session.request(method,url,
                                    data=data,
                                    json=json,
                                    **kwargs)
        try:
            return response.json()
        except Exception as err:
            return err