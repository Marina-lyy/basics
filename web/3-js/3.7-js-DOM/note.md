# DOM
- DOM Document ObjectMode；文档对象模型
- DOM是js操作文档（html文档、XML文档）的一个中间接口
- DOM操作的范围就是视窗区域，也就是浏览器的白色区域，专门用于显示HTMLLbody相关内容的位置
- DOM的本质是window对象中的一个子对象：document子对象
## 概念
- 节点
- 页面中的所有内容都是节点，无论是标签，文字，声明，注释，js都是节点
- 节点层次
- 节点之间的关系就是节点层次
# Node对象  节点对象
- 在js中所有内容都是对象创建的
- 在DOM中所有的内容都是节点创建的，节点是对象创建的

## Node对象的基本属性

### 描述属性
    nodeType 节点类型
    节点类型是用来表示内容创建使用的节点
    ELEMENT_NODE  元素节点  1   【HTML标签】
    ATTRIBUTE-NODE  属性节点  2    【标签的属性】
    TEXT_NODE   文本节点  3    【文本内容】
    CDATA_SECTION_NODE CDATA数据节点  4
    ENTITY_REFERENCE_NODE  实体字符参考节点  5
    ENTITY_NODE  实体节点  6
    PROCESSING_INSTRUCTION_NODE  处理指令节点  7
    COMMENT_NODE  注释节点  8
    DOCUMENT_NODE  文档节点  9
    DOCUMENT_TYPE_NODE  文档声明节点  10
    DOCUMENT_FRAGMENT_NODE  文档片段节点  11
    NOTATION_NODE  符号节点  12
    
    nodeName  节点名称
        元素节点  大写标签名字符串
        属性节点  属性名字符串
        文本节点  #text
        文档节点  #document
        
    nodeValue 节点值
        元素节点  null
        属性节点  属性值字符串
        文本节点  文本字符串本身
        文档节点  null
        
### 关系属性
    firstChild  获取元素、文档节点的第一个子节点
    lastChild  获取元素、文档节点的最后一个字节点
    firstChild和lastChild需要做兼容性解决方案【低版本IE】
    
    var firstChild = big.fifrstChild.nodeType == 1?big.firstChlid:big.firstChild.nextSibling;
    var lastChild = big.lastChild.nodeType == 1?big.lastChlid:big.lastChild.previousSibling;
    
    childNodes  获取指定元素的节点集合列表
      childNodes的结果是一个多节点组成数组
    parentNode  获取当前节点的父节点
      没有任何兼容性问题
    previousSibling  获取指定节点的上一个兄弟节点
    nextSibling  获取指定节点的下一个兄弟节点
    兼容性解决方案和firstChild类似
    
    注意：在IE8以下版本中所有浏览器在解析节点时，会忽略页面中所有的空白字符：在IE9以上或者其他浏览器中，所有的
    空白字符都会被解析成文本节点，所以使用时需要做兼容性处理或者删除页面中所有空白字符（不太实际，很少使用）
    
### Node节点对象的基本方法
    appendChild在父节点列表的最后插入指定的节点
      格式：父节点.appendChild（要插入的子节点）；
    insertBefore在父节点的子节点列表的指定子节点之前插入新的节点
      格式：父节点.insertBefore(要插入的节点定位的节点）
    replaceChild 使用新节点替换指定的节点
      格式：父节点.replaceChild（新节点.被替换的节点）
    removeChild 移除指定的子节点
      格式：父节点removeChild（要被移除的子节点）
    cloneNode 克隆子节点
      格式1：节点.cloneNode（）：仅仅可以当前元素节点本身
      格式2：节点.cloneNode(true):克隆当前节点及当前节点的内部所有节点
      
### 元素节点ElementNode
    元素节点时创建一切元素的基本节点
    节点属性
    
    attributes  获取当前元素的所有属性节点集合的属性
    tagName  获取当前元素节点的标签名称（值为大写字母）
    
    节点方法
    以下三个方法都是操作元素节点的属性
    getAttribute（）
        作用：获取元素节点的属性值
        格式：元素节点.getAttribute('属性名'）；
    setAttribute（）
        作用：添加或者修改元素节点的属性值
        格式：元素节点.setAttribute('属性名','属性值');
    
    removeAttribute()
        作用：添加或者修改元素节点的属性值
        格式：元素节点.removeAttribute('属性名');
    
    HTML 元素节点
    HTML元素节点是在元素节点的基础上针对HTML文档专门设计的一套操作HTML元素节点的方法和属性，更加快捷和方便
    
    HTML DOM的相关转换规则：
        1.HTML标签所具备的属性会变成js对象的成员属性直接使用
        2.class属性在转换之后会变成对象的成员属性className（因为class是保留字之一）
        3.style属性转化之后会得到一个所有css样式和值组成的集合对象（浏览器为用户操作前解析了css）
        4.在style属性对象访问指定的css样式时，如果样式名称带有-，需要变更为：去掉-，将-后面的第一个字母大写
        
### Document元素节点属性
    all  返回页面中所有HTML元素节点组成的数组
    anchors  返回页面中所有和错点相关的链接组成数组
    forms  返回页面中所有单相关节点组成的集合
    images  适合页面中所有图片元素节点组成集合
    links  返回页面中所有链接标签组成的集合（包括a标签和map中的href值）
    
    Element元素节点属性
    accessKey  设置元素操作的快捷键
        格式：元素节点.accessKey = 按键名称字符串
    注意：在不同平台用需要使用不同的功能键进行组合操作，window的功能键使用alt
    
    clientWidth  返回元素可视区域的宽度
    clientHeight  返回元素可视区域的高度
    注意：如果元素进行了隐藏式或者元素的切割处理，以上属性仅显示可以看到的区域宽高
    
    compareDocumentPosition（）比较两个元素节点的位置
      格式：元素节点1.compareDocumentPosition（元素节点2）
      
      值：
        0.表示不同一个节点
        1.两个节点不在同一个文档当中
        2.表示节点1在节点2的后面
        4.表示节点1在节点2的前面
        8.表示节点1在节点2的内部
        16.表示节点2在节点1的内部
        32.表示2个节点之间没有关系或者他们是一个元素的2个不同属性
        
    以下三个方法都是操作元素节点的属性节点