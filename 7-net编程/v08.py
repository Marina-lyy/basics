from email.mime.text import MIMEText

mail_content =\
'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>title</title>
    </head>
    <body>
    
    <h1>这是一封HTML格式邮件</h1>
    
    </body>
    </html>
'''
msg = MIMEText(mail_content, "html", "utf-8")

# 构建发送者地址和登录信息
from_addr = "1366798119@qq.com"
from_pwd = "hjpovygcxmrshhcj"

# 构建邮件接受者信息
to_addr = "1366798119@qq.com"