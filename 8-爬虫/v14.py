from urllib import request,parse
from http import cookiejar

# 创建CookieJar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, http_handler, cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''
    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"
    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "email" : "13119144223",
        "password" : "123456"
    }
    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data = data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)


if __name__ == '__main__':
    '''
    执行完login之后，会得到授权之后的cookie
    我们尝试把cookie打印出来
    '''
    login()

    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)

