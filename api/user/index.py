import requests

from common.baserequest import req
from common.checkschema import check_schema
from common.dbHelper import DBHelper

db = DBHelper()
class User:

    LOGINPATH = "/api/account/login"


    REGISTERPATH = "/api/account/register"
    def login(self,data,sql,schemaPath,session=requests):
        res = req(url=self.LOGINPATH,json=data,session=session)
        if res:
            schemaResult = check_schema(res["data"],schemaPath)
            #传进来的sql是一个元组,对元组进行拆解
            sqldata = db.query(*sql)
            return {
                **res,
                "schemeResult": schemaResult,
                "sqldata" : sqldata
            }

    def registe(self,data,sql,schemaPath,session=requests):
        res = req(url=self.REGISTERPATH,json=data,session=session)
        if res:
            schemaResult = check_schema(res["data"],schemaPath)
            #传进来的sql是一个元组,对元组进行拆解
            sqldata = db.query(*sql)
            return {
                **res,
                "schemeResult": schemaResult,
                "sqldata" : sqldata
            }