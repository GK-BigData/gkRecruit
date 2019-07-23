//报告类

var Report = function (id) {
  this.id=id;
  this.container = $('#'+id);

  var sortable = Sortable.create(document.getElementById(id));
  console.log("初始化sortable...");
  console.log(sortable);
};

//图表元素
Report.prototype.elements=[];


Report.prototype.addElement=function () {


};

Report.prototype.addChart=  function (option) {

    console.log('Report 添加图表:');
    console.log(option);
    //添加图表,
    var element = $('<div   style="background-color: blue; width: 800px;height: 400px">xxx </div>');
    // element.attr('id','1223');


    this.container.append(element);
    console.log(element[0]);

    var chart = echarts.init(element[0]);
    chart.setOption(option);


    this.elements.push(chart);

    //element.append("<a class=\"btn-floating btn-large waves-effect waves-light red\"><i class=\"material-icons\">add</i></a>");


    var  echarts_id = element.attr('_echarts_instance_');
   // 将echart 初始化后的 _echarts_instance_ 作为 div id
    element.attr('id',echarts_id);
    //设置点击时间
    element.attr('ondblclick',"editChart('"+echarts_id+ "')");

   //var sortable = Sortable.create(document.getElementById(this.id));
  //console.log("初始化sortable...");
  //console.log(sortable);


};
