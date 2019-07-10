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

    var element = $('<div style="background-color: blue; width: 800px;height: 400px">xxx </div>');
    // element.attr('id','1223');


    this.container.append(element);
    console.log(element[0]);

    var chart = echarts.init(element[0]);
    chart.setOption(option);
    this.elements.push(chart);



   //var sortable = Sortable.create(document.getElementById(this.id));
  //console.log("初始化sortable...");
  //console.log(sortable);

};
