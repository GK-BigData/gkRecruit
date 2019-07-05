// $.get("chart1",function (data) {
//
//     console.log("图表数据:");
//     console.log(data);
//
// });
var chart = echarts.init(document.getElementById('test'));
$.ajax(
    {
        url:"chart1",
        dataType:"json",
        type:"GET",
        success:function (data) {
            console.log("数据");
            console.log(data);
            chart.setOption(data.data);
        }
    }

);