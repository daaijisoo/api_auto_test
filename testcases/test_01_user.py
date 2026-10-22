from platform import android_ver

from faker import Faker

from api.user.index import User
from common.baserequest import req, logger
from common.checkschema import check_schema
from conf.globaldata import DEFAULTACCOUNT

newMobile = Faker(locale="zh_CN").phone_number()
class Testuser:

    login_success_sql = ("select id from ls_user where mobile = %s",[DEFAULTACCOUNT["account"]],1)
    register_success_sql = ("select id from ls_user where mobile = %s",[newMobile],1)


    def setup_class(self):
        self.user = User()

    def test_01_login_success(self,session):
        res = self.user.login({
            **DEFAULTACCOUNT,
            "client":2
        },self.login_success_sql,"./schema/user/login/successSchema.json",session)
        # logger.info(res)
        assert res and res["schemeResult"] and res["data"]["msg"] == "登录成功" and res["data"]["data"]["id"] == res["sqldata"][0]

    def test_02_registe_success(self,session):
        res =self.user.registe({
            "mobile":newMobile,
            "password":"admin123",
            "client":2,
            "code":None
        },self.register_success_sql,"./schema/user/registe/registeSchema.json",session)
        # assert res and res["schemeResult"] and res["sqldata"][0] and res['data']["msg"] == "注册成功"
        assert res and res["schemeResult"]