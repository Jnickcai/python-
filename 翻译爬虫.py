import requests
import json
def translation():
        translation = input("请输入要翻译的内容：")
        r = requests.post(url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule",
                        data={"i":"{}".format(translation),
                        "from":"AUTO",
                        "to":"AUTO",
                        "smartresult":"dict",
                        "client":"fanyideskweb",
                        "doctype":"json",
                        "version":"2.1",
                        "keyfrom":"fanyi.web",
                        "action":"FY_BY_CLICKBUTTION",
                        "typoResult":"false"})
        html = json.loads(r.content)
        print("翻译后的内容为："+html['translateResult'][0][0]["tgt"])
        print("*"*40)
while 1==1 :
    translation()
