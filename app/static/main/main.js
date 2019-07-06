// $.get("chart1",function (data) {
//
//     console.log("图表数据:");
//     console.log(data);
//
// });
var chart = echarts.init(document.getElementById('test'));
$.ajax(
    {
        url:"charts?zsyear=2018&chartid=各学院男女人数占比雷达图",
        dataType:"json",
        type:"GET",
        success:function (data) {
            console.log("数据");
            console.log(data);
            chart.setOption(data.data);
        },
        error:function (data) {
            console.log("请求失败!");
            console.log(data)
        }
    }

);