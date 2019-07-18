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


//div 双击后 调用设置图表参数,接受元素id
function editChart(elementid)
{

//    获取echart实例
    var echart = echarts.getInstanceByDom(document.getElementById(elementid));
    var option = echart.ge
    console.log("获取echart配置：");
    console.log(echart.getOption());

//    设置配置 ,假设现在只有图表类型
//    更新配置
//    标题
    $('#chart_title').val();

//打开配置
    slide_config.open();

    slide_config.options.onCloseEnd=function () {
        console.log("关闭编辑侧滑,图表id:"+elementid);

    }


}

function chartTest() {
 console.log("chartTest");
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

