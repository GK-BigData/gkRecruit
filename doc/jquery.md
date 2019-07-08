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



