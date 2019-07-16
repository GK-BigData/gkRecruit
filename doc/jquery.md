## 1. 设置按钮不可用

通过添加和移除 `disable` class来实现

```javascript
设置不可用
$("#buttonid").addClass('disabled')
设置可用
$("buttonid").removeClass('disabled')
```



## 2. 隐藏元素

通过设置css的display来设置显示隐藏

```
显示
 $('#progress').css('display','block');
 隐藏
     $('#progress').css('display','none');
```

## 3. 清空元素和添加元素

> Ajax请求数据刷新页面时，需要清空某个元素下面的内容，在添加上去

$('#xx').empty()	清空元素

$('#xx').append() 添加元素到里面,可以是html字符串

添加时生成属性

https://www.jb51.net/article/54815.htm

## 4.设置input输入框

$('xxx').val(要设置的值)

$('xx').val()

5. 判断数据类型

   ```javascript
   #https://www.cnblogs.com/lingdu87/p/9152806.html
   console.log(typeof str); //string
   var num=1;
   console.log(typeof num); //number
   var bn=false;
   console.log(typeof bn); //boolean
   var a;
   console.log(typeof a); //undfined
   var obj = null;
   console.log(typeof obj); //object
   var doc = document;
   console.log(typeof doc);//object
   var arr = [];
   console.log(arr); //object
   var fn = function(){};
   console.log(typeof fn); //function   
   var str="string";
   console.log(typeof str); //string
   var num=1;
   console.log(typeof num); //number
   var bn=false;
   console.log(typeof bn); //boolean
   var a;
   console.log(typeof a); //undfined
   var obj = null;
   console.log(typeof obj); //object
   var doc = document;
   console.log(typeof doc);//object
   var arr = [];
   console.log(arr); //object
   var fn = function(){};
   console.log(typeof fn); //function   
   ```

   