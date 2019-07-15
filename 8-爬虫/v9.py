'''
访问一个网址
更改自己的 User Agent 进行伪装
'''
from urllib import request, error

if __name__ == '__main__':
    url = "http://www.baidu.com"
    try:
        # 1.使用head方法伪装UA
        #headers = {}
        #headers['User-Agent'] = 'Mozilla/5.0 (iPaid; U; CPU like Mac OSX; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3'

        #req = request.Request(url, headers=headers)

        # 2.使用add_header方法
        req = request.Request(url)
        req.add_header("User_Agent", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")
        # 正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

print("DONE>............")