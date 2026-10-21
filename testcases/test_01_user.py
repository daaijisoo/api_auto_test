from platform import android_ver

from api.user.index import LOGINPATH, REGISTERPATH
from common.baserequest import req
from common.checkschema import check_schema
from conf.globaldata import DEFAULTACCOUNT


class Testuser:
    def test_01_login_success(self,db):
        res = req(url=LOGINPATH,method="POST",json={
            **DEFAULTACCOUNT,
            "client":2
        })
        sql = "select id from ls_user where mobile = %s"
        sql_data = db.query(sql,[DEFAULTACCOUNT["account"]],1)
        sql_user_id = sql_data[0]
        assert res and check_schema(res["data"],"./schema/user/login/successSchema.json") and sql_user_id == res["data"]["data"]["id"]

    def test_02_login_fail(self,db):
        res = req(url=REGISTERPATH,method="POST",json={
            "mobile": "13333333333",
            "password": "admin123",
            "client":2,
            "code":None
        })
        sql = "select * from ls_user where mobile = %s"
        sql_data = db.query(sql,"13333333333",1)
        assert res and check_schema(res["data"],"./schema/user/registe/registeSchema.json") and sql_data
