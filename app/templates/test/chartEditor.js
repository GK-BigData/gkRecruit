//图表编辑器

function ChartEditor(chartid)
{
    this.chartid = chartid;
}


ChartEditor.prototype.updateChart= function (doc)
    {
         var chart = echarts.getInstanceByDom(doc);
        //关闭后设置更新option
          console.log("侧滑关闭，开始更新....");

          var newoptions = this.updateOption(chart.getOption());

          console.log("设置新options");
          console.log(newoptions);

          chart.setOption(newoptions);
    };

ChartEditor.prototype.updateOption=  function (options)
    {
        //获取所有class有config的input标签
        var allInput = $('input.config');

        console.log("所有输入框:");
        console.log(allInput);

        //生成的option 和图表的合并
        allInput.each(function (index,element) {


            var id=element.getAttribute('id');
            var value =$(element).val();
            var type = element.getAttribute('data-type');
            var code = 'options';

             var keys = id.split('-');

            //一级一级的key
             for(var i = 0;i<keys.length;i+=1)
             {
                 //第一个是空的
                 if(keys[i]==='')continue;

                 code+='["'+keys[i]+'"]'
             }

             //输入框是字符串的加个双引号
            if(type==='text')value='"'+value+'"';


            code+=('='+value);

            console.log("input 类型:"+type);
            console.log(code);
            //生成代码来执行，如 options["markPoint"]["0"]["label"]["show"]=true
            eval(code);

        });
       // 根据id生成如 options['xx']['yy']=zzz这样的
        options["textStyle"]["fontSize"]=22;
        return options;


    };

//生成Options菜单，循环调用
ChartEditor.prototype.optionMenu=function(option,parentDom,parentkey,level){

        //
        var ul = document.createElement('ul');

        ul.setAttribute('class','col collapsible');
        //每个子的相对于父元素缩进20,形成一种层级的效果
        ul.setAttribute('style','margin-left:20px;');

        var childrenCount = 0;
        //遍历键值对,即遍历options对象
        for (var key in option)
         {
             childrenCount+=1;

             var value = option[key];
             var type = typeof  value;

             var id=parentkey+'-'+key;

             console.log("id:"+id);

             var li = document.createElement('li');


             //{#生成 key 和 valude 的div #}
             var header = document.createElement('div');
             header.setAttribute('class','collapsible-header');
             var body = document.createElement('ul');
             body.setAttribute('class','collapsible-body');

             if (type==='string')
             {
                 console.log("value :"+li);

                 li.append(newinput(key,value,id,'text'))
             }
             else if(type==='number')
             {
                li.append(newinput(key,value,id,'number'))
             }
             else if(type==='boolean')
             {
                li.append(newinput(key,value,id,'boolean'))
             }
             //数组和对象都属于object,数组的key是0,1,2,3...
             else if(type==='object')
             {
                 //二级菜单,里面的内容是递归生成
             header.innerHTML=key+" ";
             var count = optionMenu(value,body,id,level+1);

             $(li).append(header).append(body);

             }


            $(ul).append(li);


        }

        $(parentDom).append(ul);
        //{#    返回有多少个#}
        return childrenCount;
};

//生成配置 ,图表id和存放输入框的容器，读取option,生成容器

ChartEditor.prototype.generateConfig=function(chartid,container){

            var chart = echarts.getInstanceByDom(document.getElementById('chart'));

            console.log("生成图表配置,原配置:");
            console.log(chart.getOption());

            //{# 存放配置的容器#}
            var container = document.getElementById('option');
            console.log('清空原容器..');
            $(container).empty();

            //填充菜单到容器
            this.optionMenu(chart.getOption(),container,'',0);

            console.log("初始化..");

            //初始化伸展菜单
            M.Collapsible.init(document.querySelectorAll('.collapsible'));

};