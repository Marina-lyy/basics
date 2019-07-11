import urllib

if __name__=='__main__':
    url = "https://jobs.zhaopin.com/CC137615181J00136490510.htm"
    # 打开相应URL并把相应页面作为返回
    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))

    html = rsp.read()

    html = html.decode()
