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
    
## 清除定时执行
    clearTimeout（）取消定时执行的操作
    格式：clearTimeout（定时变量）；
    
## 清除循环执行
     clearInterval（） 取消循环执行操作
     格式：clearInterval（循环变量）
     
## 浏览器的三种弹窗
    alert（） 系统警告弹窗
        作用：用于弹出窗口警示用户，提示信息
        
    confirm（） 系统默认弹窗
        作用：根据用户的行为进行不同的操作
        返回值：确定->true  取消->false
        
    prompt() 系统输入弹窗
        作用：用于接收用户在弹窗输入的内容字符串
        格式：
            变量 = prompt（’提示信息字符串‘，’默认值字符串‘）；
        返回值：用户输入的信息
        
## 浏览器打开和关闭页面的方法和属性：
    open（）  打开一个新的页面
        格式：变量 = open（‘url地址’，‘打开方式’，‘打开页面的属性’，是否替换原有页面）；
        参数3：页面属性相关参数：
        width  设置打开页面的宽度
        height  设置打开页面的高度
        left  设置打开页面的距离屏幕左侧的距离
        top  设置打开页面距离屏幕顶部的距离
        location  设置是否允许出现地址栏  yes 允许  no不允许
        status  设置是否显示状态栏
        resize  设置是否允许调整弹出页面的大小  yes 允许  no 不允许
        toolbar  设置是否允许显示工具栏  yes 允许 no不允许
        menubar  设置是否允许显示工具栏  yes 允许  no不允许
        scrollbars  设置是否允许滚动页面  yes允许  no不允许
        
        注意：在现在的高板本浏览器中，所有open方法打开的页面，均被认为是公告弹窗，会自动禁止
        
        open方法中涉及到的新页面属性在部分浏览器中不支持
        
        多个属性的格式：属性=值，属性=值，属性=值。。。。
        
        参数4：设置是否替换原有页面
        
        true  替换原有页面（不会有后退按钮操作）
        false  不替换原有页面（会有后退按钮操作）
        
    close（）  关闭页面操作
        格式：window变量.close（）
    注意：close方法仅可以关闭当前页面存在打开关系的页面
    closed 页面是够处于关闭状态的属性
        格式：window变量.closed 
        true 表示页面已关闭    false  表示页面未关闭
        
## 页面焦点方法
    focus（）  获取焦点的方法
    blur()  失去焦点的方法
    
## 关系属性
    top
        在框架集合页面中使用，表示当前页面的顶部页面的window对象
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
