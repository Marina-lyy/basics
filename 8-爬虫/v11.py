from urllib import request,error

if __name__ == '__main__':
    url = "https://passport.baidu.com/center?_t=1563169547"

    proxy = {'http':'120.194.18.90:81'}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)

        #print(rsp.read().decode())
        html = rsp.read().decode()

        with open("rsp.html","w") as f:
            f.write(html)

    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)


