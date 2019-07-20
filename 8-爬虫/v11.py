from urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/971519057/profile"

    rsp = request.urlopen(url)

    #print(rsp.read().decode())
    html = rsp.read().decode()

    with open("rsp.html","w") as f:
        f.write(html)



