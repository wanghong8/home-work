#_*_ coding:utf-8 _*_
import re
class yanzheng():
    def __init__(self,number,email):
        self.number=number
        self.email=email
    def is_phone(self):
        if re.match("^1[3|4|5|6|7|8][0-9]\d{8}$",self.number):
            print("正常手机号")
        else:
            print("非正常手机号")
    def is_email(self):
        if re.match("^.+\\@(" "\\[?)[a-zA-Z0-9\\-\\_\\.]" "+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",self.email):
            print("正常邮箱")
        else:
            print("非正常邮箱")

a=yanzheng("11566868970","1908199861@qq.com")