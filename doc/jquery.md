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