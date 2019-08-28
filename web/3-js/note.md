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
    