//报告类

var Report = function (id) {
  this.id=id;
  this.container = $('#'+id);

  var sortable = Sortable.create(document.getElementById(id));
  console.log("初始化sortable...");
  console.log(sortable);
};

//图表元素
Report.prototype.elements={};


//添加一个成员到报告界面
Report.prototype.addElement=function (element) {

    console.log('添加元素,类型:'+element.type);
//    生成一个随机id
    var random_id = element.type+ Math.round(Math.random()*10000000);
    console.log('生成随机id',random_id);
//    查看添加的成员类型
    if(element.type==='chart')
    {
        this.addChart(element.option,random_id);
    }

//    保存数据到全局字典
    this.elements[random_id]=element;


};

//获取图表
/*
添加图表
1. 生成div ，添加到容器
2. 初始化图表，设置options
// 3.添加到所有成员
// 4.设置div id为echart_instance属性的值
5.设置双击事件为打开这个图表
 */
Report.prototype.addChart=  function (option,id) {

    console.log('Report 添加图表,option:');
    console.log(option);
    //添加图表,
    var element = $('<div   style="background-color: blue; width: 800px;height: 400px">xxx </div>',{
        id:id
    });
    //上面的id设置不行
    element.attr('id',id);


    this.container.append(element);
    console.log(element[0]);

    var chart = echarts.init(element[0]);
    chart.setOption(option);




    //element.append("<a class=\"btn-floating btn-large waves-effect waves-light red\"><i class=\"material-icons\">add</i></a>");



    //var  echarts_id = element.attr('_echarts_instance_');
   // 将echart 初始化后的 _echarts_instance_ 作为 div id
    //element.attr('id',echarts_id);
    //设置点击时间
    element.attr('ondblclick',"editChart('"+id+ "')");

   //var sortable = Sortable.create(document.getElementById(this.id));
  //console.log("初始化sortable...");
  //console.log(sortable);


};
