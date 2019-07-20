from urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/971519057/profile"

    headers = {
        "Cookie": "anonymid=jy3yhwba-vvj0w8; depovince=GW; _r01_=1; __guid=238633222.3138273734904068600.1563169059070.871; JSESSIONID=abcYSuFDh7eZ8gKU0l_Vw; ick_login=799163a5-cc53-46cc-a870-af6adf6a5f28; id=971519057; ver=7.0; loginfrom=null; jebe_key=1d9c66bc-d49c-4b12-b545-2e8c3f4930a9%7C15440b0cbb6d214f08c0b3f695b3b299%7C1563338791580%7C1%7C1563338790383; jebe_key=1d9c66bc-d49c-4b12-b545-2e8c3f4930a9%7C15440b0cbb6d214f08c0b3f695b3b299%7C1563338791580%7C1%7C1563338790392; wp_fold=0; t=da9dcde5c720b46b95395fe974db2aa17; societyguester=da9dcde5c720b46b95395fe974db2aa17; xnsid=fcae605e; jebecookies=1d19964b-b710-4370-8059-725a08129e59|||||; monitor_count=8"
    }
    req = request.Request(url,headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open("rsp.html","w") as f:
        f.write(html)