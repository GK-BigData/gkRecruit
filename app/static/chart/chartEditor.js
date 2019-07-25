//图表编辑器封装
//生成图表配置，根据配置生成options
function ChartEditor()
{

    //图表配置项字典
    this.dict={
     'color':'颜色',
  'title':'标题',
  'series':'序列',
  'markArea':'标记区域',
  'markLine':'标记线',

    }

}

ChartEditor.prototype.setChartId=function(id)
{
    this.chartid=id;
};

ChartEditor.prototype.updateChart=function()
{
    if(this.chartid===undefined)
    {
        console.log("图表id未设置.更新图表失败!");
        return;
    }
    this.updateChartByDocument(document.getElementById(this.chartid));
};
ChartEditor.prototype.updateChartByDocument= function (doc)
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

                 li.append(this.newinput(key,value,id,'text'))
             }
             else if(type==='number')
             {
                li.append(this.newinput(key,value,id,'number'))
             }
             else if(type==='boolean')
             {
                li.append(this.newinput(key,value,id,'boolean'))
             }
             //数组和对象都属于object,数组的key是0,1,2,3...
             else if(type==='object')
             {
                 //二级菜单,里面的内容是递归生成
             header.innerHTML= this.translate( key)+" ";
             var count = this.optionMenu(value,body,id,level+1);

             $(li).append(header).append(body);

             }


            $(ul).append(li);


        }

        $(parentDom).append(ul);
        //{#    返回有多少个#}
        return childrenCount;
};



//生成配置 ,图表id和存放输入框的容器，读取option,生成容器
ChartEditor.prototype.generateConfig=function(container)
{
        this.generateConfigByChartId(this.chartid,container);
};

ChartEditor.prototype.generateConfigByChartId=function(chartid,container){

            var chart = echarts.getInstanceByDom(document.getElementById(chartid));

            console.log("生成图表配置,原配置:");
            console.log(chart.getOption());

            //{# 存放配置的容器#}
            //var container = document.getElementById('option');
            console.log('清空原容器..');
            $(container).empty();

            //填充菜单到容器
            this.optionMenu(chart.getOption(),container,'',0);

            console.log("初始化..");
            //初始化伸展菜单
            M.Collapsible.init(document.querySelectorAll('.collapsible'));

};
ChartEditor.prototype.translate=function(key)
{
         if( key in this.dict)
        {
           return  this.dict[ key] +"("+key+")";
        }
        else
        {
            return key;
        }
};
// 生成input标签  type数据类型,字符串为text,数字为number,boolean，因为在更新options时需要获取对应的类型，字符串就加入
ChartEditor.prototype.newinput=function (key,value,id,type) {
        var div = $('<div class="input-field"></div>');
        var input = $('<input/>',{
            id:id,
            type:'text',
            //config用于识别是不是配置的输入框，更新options时通过这个来获取
            class:'validate config',
            value:value,
            'data-type':type

        });
        //label可以翻译为正常的文字
        var label = $('<label></label>',{
            for:id,
            class:'active'
        });
        label.html(this.translate(key));


        div.append(input);
        div.append(label);

        return div[0];
    };