# js基础
- 什么是js？
- js的全称是Javascript
##### java和JavaScript有什么关系？
    老婆和老婆饼的关系
    李明和李明海的关系
    雷锋和雷峰塔的关系
    JavaScript和java之间基本没有任何关系！
##### JavaScript的历史
    JavaScript有规范 -》 ECMA组织制定ECMAscript语法规范
    JavaScript是由早期网景公司开发的，JScript是由微软开发的
    目前而言JScript和JavaScript基本上是同一个东西
    
##### 如何使用js代码
    在html中可以使用script标签引入js文件或者代码。
    
    src属性  用于引入js文件的地址
    language属性  设置脚本的语言类型（已经废弃）
    type属性  用于设置引入文件的IME类型
    charset属性  用于设置引入js文件的字符集类型
    defer属性  延时执行属性，可以使得js在html完全加载完毕之后才执行。（对外部js文件有效）
    async属性  异步加载属性，js下载中的VIP，注意，仅改变下载顺序不改变执行顺序
    
## 三种js的使用方式
    外链式js
        <script src="文件路径"></script>
        
    嵌入式js
        <script>
            书写js代码；
        </script>
        
    内联式js
        <button 事件属性="js代码">按钮名称</button>
        
    推荐格式：
        1.js的框架文件，一般使用外链式js。
        2.局部性的js代码可以使用嵌入式js
        3.内联式js尽量少用。
        
## js基本语法
#### 变量
    什么是变量？
    x+y = 10  x=4  y=?  x=1  y=?  x=7  y=?
    可以改变的量就是变量。
    
    声明规范：
    var  变量名 = 值：  //声明并且赋值
    案例js_06
    var  变量名：      //声明但是不赋值
    案例js_07
    变量 = 值：       //不使用var关键字声明（不推荐）
    案例js_08
    
    变量的规则：
    1.声明变量必须使用var关键字
    2.可以使用中英文当做变量名，但是不推荐使用中文。
    3.可以使用数字，但是不能用数字开头。
    4.不可以使用特殊字符，除了$和_(下划线）
    5.变量名严格区分大小写。
    6.变量的命名尽量有意义
    7.变量名称不能和系统的保留关键字冲突。
    
    关键字：
    break  do  instanceof  typeof
    case  else  new  var  in  try
    catch  finally  return  void
    continue  for  switch  while
    debugger  if  throw  delete
    
    保留字
    abstract  enum  int  short 
    boolean  export  interface  static
    byte  extends  long  syper
    char  float  package  throws
    const  goto  private  transient
    debugger  implements  protected  volatile
    double  import  public
    
    如何避免和保留字关键字冲突
    使用大写字母
    使用特殊字符号$_
    使用拼音
    背下来保留字和关键字
    
### js注释的分类
    单行注释
        //单行注释
    多行注释
        /*
           多行注释
     */
     注意：多行注释禁止嵌套多行注释
     
## js中的数据类型分类
    一种类型：（对象）
    js中所有数据都是由对象创建的，因为js是一门基于对象的语言
    
    两种类型：（简单数据类型和复杂数据类型/基本数据类型和引用数据类型）
    简单数据类型（基本数据类型）
        常见数值，整数，小数，字符都是简单数据类型
    复杂数据类型（引用数据类型）
        对象。
        
    六种类型：使用数据检测语法typeof检测的结果
    undefined   类型
    string      字符串类型
    number      数值类型
    Boolean     布尔类型
    function    函数类型
    object      对象类型
    
    undefined类型
    undefined类型只有一个值，就是undefined本身。
    获得undefined值的方式有2种：
        1.声明变量但是不赋值，默认值为undefined
        2.为变量直接赋值为undefined
    注意：如果没有特殊需求，不需要直接设置undefined。
    案例js_10
    
    string类型  字符串类型
    string类型就是字符串类型，声明的时候需要使用引号
    
    声明字符串的方式有2种：
        1.单引号声明字符串
        2.双引号声明字符串
    注意：只要声明时使用了单双引号，无论是数字内容还是其他的undefined单词内容，最终类型都会变成字符串。
    
    单引号和双引号是否存在区别：
        单双引号都不可以解析变量
        单双引号都可以解析转义字符
        单双引号可以互相插入。
    案例js_11
    
    number类型
    number类型可以分为三张类型：整数型，浮点型和nan类型
    整形的声明方式；
        var val = 250; //十进制声明方式
        var val = 0177;  //八进制声明方式
        var val = 0xff00;  //十六进制声明方式
    
    浮点型的声明方式：
        var val = 250.41; //小数方式声明浮点类型
        var val = 3.141592653e5;  //科学计数法
        
        var val = .5;  简写方式1（禁止使用）
        var val = 5.； 简写方式2（禁止使用）
    注意：浮点型没有分数表示方式  1/4不是分数而是一个运算表达式
    
    NaN类型：
        NaN    Not a Number    不是一个数值
        获得NaN的方式：
            var val = 5 - ‘a';  //数字和字符串进行了乘法运算。（错误运算）
            var val = NaN；  //直接赋值为NaN
            
        注意：尽量避免获得NaN值，因为NaN是个错误！
        
        NaN的特点：
        1.NaN不等于任何数值，包括NaN自己
        2.NaN具有传染性，任何和NaN之间运算的结果都是NaN
        3.唯一检测NaN的办法是使用isNaN（）功能
    案例js_12
    
    Boolean类型
    布尔类型只有2搁置：TRUE 和 FALSE
    TRUE表示真值
        真值表示确定的意思，有，对，是！ 好的，
    FALSE表示假值
        假值表示否定的意思，没有，不对，不是，不行！
    注意：TRUE和FALSE都是小写，而且绝对不允许使用引号
    案例js_13
    
    function类型
    分为两类：声明函数和表达式函数
    声明函数
        function val(){
            alert('奥运金牌今年不是很多啊！');
            }
            
    表达是函数/匿名函数
        var val(){
            alert('奥运金牌今年不是很多啊！');
            }
    案例js_14
    
    object类型
    什么是对象？
        对象是数据和功能的集合
    创建一个简单的对象
        var val = new object（）；
    对象中的特殊对象null
        null是对象类型和空指针
        
    undefined和null的区别：
        1.undefined是undefined类型，null是对象类型
        2.undefined和null的值相同。
        
        undefined  无业游民  null  待业青年
        
        undefined类型并不知道未来数据类型是什么。
        null的未来数据类型就是对象
        案例js_15
            
    转义字符
    \n     换行                        换到下一行
    \r     回车(不是回车键）           回到当前行的开头
    \t     缩进        
    \\     表示一个\
    \'     表示一个单引号
    \"     表示一个双引号

    回车按键：
        根据操作系统不同，得到的是完全是不同的字符
        Windows       \r\n
        linux         \n
        macos         \r (10.9)  或者  \n  (>10.9)
        案例js_11
        

# 数据类型转换
    什么是数据类型转换
    将一个数据当前类型转换为其他类型的过程就是数据类型的转换
#### 数据类型转换的分类
    显示数据类型转换（强制数据类型转换）
    隐式数据类型转换（自动数据类型转换）
    
## 隐式数据类型转换
    在程序执行过程中根据需要发生的数据类型转换，不经过人工干预，这就是自动数据类型转换
    1.自动类型转换多发生在运算或者判断过程当中
    2.不需要人工干预。
    3.自动类型转换向着更加精确的方向转换
    案例：js_16
## 显示数据类型转换
    根据程序员自己的意愿进行的数据类型转换，需要进行操作
    Number
    undefined
    string
    Boolean
    function
    object
#### Number数据类型转换
    parseInt  强制将一个字符串类型转换为整型（注意仅对字符串类型有效）
    转换格式：新变量 = parseInt（原变量)
    转换规则：
        1.如果是纯数值字符串，将该数值直接转换为整形（取消小数点后面的数值）
        2.如果是以数值开头的字符串，将第一个非数值值之前的数值部分保留，删除所有第一个非数值字符串之后的内容，然后将保留的数值部分转换为整形（取消小数点后面的数值）
        3.如果不是数值开头的字符串，转换结果永远为NaN
    
    parseFloat  强制将一个字符串类型转换为浮点类型（注意：仅对字符串类型有效）
    转换格式：新变量 = parseFloat（原变量）
    转换规则：
        1.如果是纯数值字符串，将该数值直接转换为浮点型
        2.如果是以数值开头的字符串，将第一个非数值之前的数值部分保留，删除所有第一个非数值字符串之后的内容，然后将保留的数值部分转换为浮点型
        3.如果不是数值开头的字符串，转换结果永远为NaN
        
    Number 将任意类型数据转换为Number类型
    转换格式：新变量 = Number（原变量）
    转换规则：undefined - NaN
              Number    - 不需要转换
              string    - 纯数值转换为对应的数值  非纯数值 - NaN
              Boolean   - TRUE  -》1   FALSE  -》 0
              function  - NaN  
              object    -NaN      null =》0
              
#### 布尔类型转化
    Boolean将任意类型转换为布尔值
    转换格式：新变量 = Boolean（原变量）；
    转化规则：
        1.Number  -》  0  /  0.0/ NaN
        2.string ->  空字符串 “”
        3.undefined - 》 永远是FALSE
        4.Boolean - 》 FALSE
        5.function -》 永远为真
        6.object -》 null为FALSE，其余都是真
       
#### 字符串类型转换
    string将任意类型转换为字符串
    转换格式：新变量 = string（原变量）；
    转换规则：
        1.undefined  -》 ‘undefined’字符串
        2.number     -》  转换为对应的数值字符串或者‘NaN’字符串
        3.string     -》   不需要转换
        4.Boolean    -》   ‘TRUE’ 或者‘FALSE’
        5.function   -》   字符串的函数结构
        6.object     -》   【object  object】对象结构表示形式字符串
        
    变量.toString将任意类型转换为字符串（特殊的值不能用）
    注意：undefined值和null值无法使用
    转换格式：
        新变量 = 原变量.toString()
    转换规则：
        和String的转换规则一致。
    
      


   
    







    