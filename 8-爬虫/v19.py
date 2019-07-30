'''
v2
处理js加密代码
'''
'''
通过查找，能找到js代码中操作代码
1.这个是计算salt的公式 i = r + parseInt(10 * Math.random().10);  r = "" + (new Date).getTIme().
2.sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
md5 一共需要四个参数，第一个和第四个都是固定值的字符串，第三个是所谓的salt，第二个是。。。
第二个参数就是输入的要查找的单词
'''
def getSalt():
    '''
    salt公式是   "" + (new Date).getTIme()+ parseInt(10 * Math.random().10);
    把他翻译成python代码
    :return:
    '''
    import time, random
    salt = int(time.time()*1000)+random.randint(0,10)

    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    # update需要一共bytes格式的参数
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()

    return sign

def getSign(key,salt):
    sign = 'fanyideskweb' + key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"

    sign = getMD5(sign)
    return sign

from urllib import request,parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = getSalt()
    data = {
        "i":key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":str(salt),
        "sign":getSign(key,salt),
        "ts":"1563790987015",
        "bv":"bbb3ed55971873051bc2ff740579bb49",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME"
    }
    print(data)
    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept":"application/json,text/javascript,*/*;q=0.01",
        #"Accept-Encoding": "gzip,deflate",
        "Accept-Language":"zh-CN,zh;q = 0.9",
        "Connection":"keep-alive",
        "Content-Length":len(data),
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
    youdao("salt")
