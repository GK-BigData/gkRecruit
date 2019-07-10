// $.get("chart1",function (data) {
//
//     console.log("图表数据:");
//     console.log(data);
//
// });
var chart1 = echarts.init(document.getElementById('test1'),'vintage');

$.ajax(
    {

        url:"charts?zsyear=2018&chartid=男女人数排三的专业",
        dataType:"json",
        type:"GET",
        success:function (data) {

            console.log("数据");
            console.log(data);
            chart1.setOption(data.data);

            baseOptions['男女人数排三的专业']=data.data;

            console.log('基本配置');
            console.log(baseOptions);
        },
        error:function (data) {
            console.log("请求失败!");
            console.log(data)
        }
    }

);


//添加元素到列表,从baseOptions里找
function addChart(elementid)
{
    console.log('添加图表,id:'+elementid);
    console.log(report);
    report.addChart(baseOptions[elementid]);

}

//加载模板
function loadBaseOption()
{




}


//所有模板的options
var baseOptions = {};



var report = new Report("report");
console.log("初始化..");
console.log(report);

