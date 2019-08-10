# 创建HTML文件
- 文件名部分
    1. 使用英文数组下划线或者 - 等字符组成
    2. 请尽量有意义
    3. 不要随便使用空格和特殊字符
- 文件后缀部分
.html后缀
    win2000年后对文件的后缀长度不做限制，后缀就开始变得完整了
    比如：.doc->.docx  .txt->.text  .jpe->.jpeg  .htm->.html
.htm后缀
    在早期的win98操作系统中，只能够支持三位数的文件后缀，所以那个时候诞生的文件，都是三位数以内的后缀。
    比如：.doc word文档   .avi  视频文件  .txt  文本文件  .jpg/jpe 图片文件
- 注意：组织->文件和文件夹选项-> 查看选项卡->高级设置部分->去掉“隐藏已知文件类型的扩展名”的勾

# 第一个HTML代码
    <marquee>什么是图灵？图灵就是秃了就会灵光一现，顿悟！</marquee>
- 总结特征/基本结构：
                  <标签名>内容</标签名>
                  
        <marquee width="50%">什么是图灵？图灵就是秃了就会灵光一现，顿悟！</marquee>
- 总结特征/结构2：
                  <标签名 属性名="属性值">内容</标签名>

        <marquee width="50%" loop="2">什么是图灵？图灵就是秃了就会灵光一现，顿悟！</marquee>
- 总结特征/结构3：
                  <标签名 属性名="属性值" 属性名="属性值">内容</标签名>
- 注意：HTML标签属性没有顺序限制.

           <marquee loop="2" width="50%">
               <font color="pink">什么是图灵？图灵就是秃了就会灵光一现，顿悟！</font>
           </marquee>
- 总结特征/结构4：
                    <标签名1 属性名="属性值" 属性名="属性值">
                        <标签名2 属性名="属性值">内容</标签名2>
                    </标签名1>
- 注意事项：
   - 1.所有的单词字母符号，都必须在英文半角下输入
   - 2.标签非常多则么办？多写多练
   - 3.标签对应的属性非常多？多写多练
- 注释：注解和解释，说明文字，不会被浏览器识别，只是用于程序员或者开发人员之间沟通和说明
# HTML标签的学习
## 全局架构标签
        <!doctype html>
        <html>
            <head>
                <!--网页的思想 都是看不到信息-->
                <meta charset="utf-8">
            </head>
            <body>
                <!--网页的显示主题  都是看不到信息-->      
                为什么男人用符号♂，女人的符号用♀，我觉得很不妥！明显男人应该用%，女人用@符号，这才贴切！
            </body>
        </html>
 ## 标签详解
 #### body标签
    bgcolor属性       用于设置页面的背景颜色
    background属性    设置页面的背景图片
    注意：如果同时存在背景颜色和背景图片，优先显示背景图片
    了解属性：
     

                  