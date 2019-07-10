'''
利用request下载页面
自动检测页面编码
'''

import urllib
import chardet
if __name__ == '__main__':
    url = "http://data.eastmoney.com/stockdata/600696.html"

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    # 利用 Chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 使用get取值保证不会出错
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)
