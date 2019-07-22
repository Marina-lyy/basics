'''
破解有道词典
'''
from urllib import request,parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i":"girl",
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"15637909870157",
        "sign":"4a0723bbea9da1d1603775d8fecd3958",
        "ts":"1563790987015",
        "bv":"bbb3ed55971873051bc2ff740579bb49",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME"
    }
    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept":"application/json,text/javascript,*/*;q=0.01",
        #"Accept-Encoding": "gzip,deflate",
        "Accept-Language":"zh-CN,zh;q = 0.9",
        "Connection":"keep-alive",
        "Content-Length":"237",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie":"OUTFOX_SEARCH_USER_ID=-634845217@10.108.160.19;JSESSIONID=aaaU0yOA9qg276kxpmzWw;__guid=204659719.2196758183266424800.1563790727090.909;OUTFOX_SEARCH_USER_ID_NCOO=695549491.9475253;monitor_count=3;___rl__test__cookies=1563791823659",
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.132Safari/537.36X-Requested-With:XMLHttpRequest"
    }
    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("girl")