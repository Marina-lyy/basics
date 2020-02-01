# BOM
## 什么是BOM？
- Browser Object Model 浏览器对象模型

## BOM的作用是什么？
- BOM的作用是用于连接JS语言和浏览器行为的一个中间结构。
- 如果浏览器是空调的话，BOM就是遥控器
- JS可以通过操作BOM，实现浏览器的行为变化

## BOM的本质
- BOM是JS可以操作的内容，所以他的本质是对象，BOM在js中是一个对象，window对象就是BOM本身

# window对象分析：
    window对象代表浏览器本身：
        document    表示浏览器的文档部分（文档对象）DOM
        location    表示浏览器位置相关的对象
        frames      表示浏览器框架集相关信息的对象
        history     浏览器历史信息对象
        screen      浏览器屏幕信息对象
        navigator   浏览器信息对象
## window对象自身的功能
    浏览器的宽度和高度属性
    适用于高版本IE和其他浏览器
    innerwidth  表示浏览器视窗的宽度
    innerHeight 表示浏览器视窗的高度
    
    低版本IE浏览器获取浏览器视窗宽高的方法：
    
    document.documentElement.clientWidth
    document.documentElement.clientHeight
    
## 浏览器位置信息属性
    非Firefox浏览器识别属性
    screenLeft  浏览器距离屏幕左侧的距离
    screenTop   浏览器距离屏幕顶部的距离
    Firefox 浏览器
    screenX     浏览器距离屏幕左侧的距离
    screenY     浏览其距离屏幕顶部的距离
    
## 浏览器窗口大小调整方法
    resizeTo（）  将浏览器设置为指定的宽度和高度
        格式：resizeTo（宽度，高度）；
    resizeBy（）  将浏览器在当前宽高的基础上增加或者减少指定长度的宽高
        格式：resizeBy（水平长度，垂直长度）
        如果长度为正数，则增加，为负数，则减小
    注意：以上方法必须在单标签浏览器中使用

## 浏览器位置大小调整方法
    moveTo（）  将浏览器移动到指定的坐标
        格式：moveTo（水平坐标，垂直坐标）；
    moveBy（）  将浏览器在当前位置基础上移动指定的长度
        格式：moveBy（水平长度，垂直长度）；
        如果长度为正数，则向下或者向右移动，负数则向上或者向左移动
        
    注意：以上方法必须在单标签浏览器中使用
    
## 定时执行
    setTimeout() 设置定时执行操作
    格式：定时变量 = setTimeout（回调函数，时间）；
    方法1：setTime（函数名，时间）；
    方法2：setTimeout（匿名函数，时间）；
    方法3：setTimeout（‘调用函数的字符串’，时间）
    
## 循环执行
    setInterval（）循环执行方法
    格式：循环变量 = setInterval（回调函数，时间）；
    方法1：setInterval（函数名，时间）；
    方法2：setInterval（匿名函数，时间）；
    方法3：setInterval（‘调用函数的字符串’，时间）
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
