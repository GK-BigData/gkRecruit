// $.get("chart1",function (data) {
//
//     console.log("图表数据:");
//     console.log(data);
//
// });

//图表编辑工具
var chartEditor = new ChartEditor();


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


/*
加载数据源到下拉框,即record
*/
function loadDataSource()
{

    $.get('/admin/records',function (data) {

        console.log("获取数据源..");
        console.log(data);
        if(data.code===0)
        {

            //填充select
            var select = $('#datasource');
            data.data.forEach(function (ele,index) {
               console.log(ele);
               var option = $('<option></option>',{
                   id:ele.id
               });
               option.text(ele.id+ " "+ele.zsyear+ " "+ ele.status);

                select.append(option);
            });


             M.FormSelect.init(document.getElementById('datasource'));

        }
        else {
            console.log("获取数据源失败!!");
        }

    })


}



//添加元素到列表,从baseOptions里找
function addChart(elementid)
{
    console.log('添加图表,id:'+elementid);
    console.log(report);
    report.addChart(baseOptions[elementid]);

}


/*
div 双击后 调用
1.接受div id
2.设置chartEditor 的chartId
3.打开侧滑配置
4.生成配置的input等标签

*/
function editChart(elementid)
{
    //设置当前编辑的图表
    chartEditor.setChartId(elementid);

    //打开配置侧滑
    slide_config.open();

    // slide_config.options.onCloseEnd=function () {
    //     console.log("关闭编辑侧滑,图表id:"+elementid);
    //
    // };
    chartEditor.generateConfig(document.getElementById('container'));


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

loadDataSource();

