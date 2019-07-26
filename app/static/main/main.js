"use strict";
// $.get("chart1",function (data) {
//
//     console.log("图表数据:");
//     console.log(data);
//
// });

//图表编辑工具
var chartEditor = new ChartEditor();


// var chart1 = echarts.init(document.getElementById('test1'),'vintage');
//
// $.ajax(
//     {
//
//         url:"charts?zsyear=2018&chartid=男女人数排三的专业",
//         dataType:"json",
//         type:"GET",
//         success:function (data) {
//
//             console.log("数据");
//             console.log(data);
//             chart1.setOption(data.data);
//
//
//             baseOptions['男女人数排三的专业']=data.data;
//
//             console.log('基本配置');
//             console.log(baseOptions);
//         },
//         error:function (data) {
//             console.log("请求失败!");
//             console.log(data)
//         }
//     }
//
// );

/*
请求图表数据的参数
返回 要提交的参数
 */
function getCreateChartParams()
{
    //要重新init，不然获取到的是上一次的值
    //分组字段
      var select_groupfields = M.FormSelect.init(document.getElementById('groupfield'));
      //聚合字段
      var select_aggfields = M.FormSelect.init(document.getElementById('aggfield'));

      //var select_dataType = M.FormSelect.init(document.getElementById('dataType'));
     var  select_chartType = M.FormSelect.init(document.getElementById('chartType'));
     var  select_orderBy = M.FormSelect.init(document.getElementById('orderBy'));

    var groupfield = select_groupfields.getSelectedValues();
    var aggfield = select_aggfields.getSelectedValues();

   // var dataType = select_dataType.getSelectedValues();
    var chartType = select_chartType.getSelectedValues();
    var orderBy = select_orderBy.getSelectedValues();


    var limit = $('#limit').val();
    console.log("获取创建图表参数..");

    console.log(groupfield);
    console.log(aggfield);

   // console.log(dataType);
    console.log(chartType);

    return {
        aggfield:aggfield.join(','),
        groupfield:groupfield.join(','),
        //dataType:dataType[0],
        chartType:chartType[0],
        orderBy:orderBy[0],
        limit:limit,
        //当前的数据的ID
        recordid:recordid,
        dataType:'group',
        //filter:'total_score_of_filing->=-200'
        filter:'null'
    }

}
/*
这个是预览按钮的点击时间
在创建图表之前预览
//请求数据，返回option ,设置在chart上
 */
 var preview_chart ;
function previewChart()
{

    //初始化图表
    if(preview_chart===undefined) preview_chart= echarts.init(document.getElementById('preview_chart'));
    console.log("创建图表之预览图表");

    //设置为黑色
    Zs.prototype.disable('#preview');

    var params = getCreateChartParams();
    console.log("获取提交参数:");
    console.log(params);


    $.ajax({
        url:'charts2',
        type:'POST',
        data:params,
        dataType:"json",
        success:function (data,status) {

        console.log("图表返回结果:");
        console.log(data);
            if(data.code===0) {

               preview_chart.clear();
                preview_chart.setOption(data.data.option);
            }
             else
             {
                    showJsonResult(data);
              }

        },
        error:function (data) {
            console.log("请求失败");
        }


    });

    // $.post('charts2',params,function(data){
    //
    //      var preview_chart = echarts.init(document.getElementById('preview_chart'));
    //
    //     console.log("图表返回结果:");
    //
    //     console.log(data);
    //     console.log(data.data);
    //
    //     if(data.code===0)
    //         preview_chart.setOption(data.data);
    //     else
    //     {
    //
    //     }
    //
    //
    // });
    Zs.prototype.enable('#preview');


}
/*
创建图表到侧滑栏，
点击创建按钮的时间
 */

function createChart()
{

    var params = getCreateChartParams();
    createChartByParams(params);


}
//更新侧滑的基本元素 的图表
function updataBaseOptions()
{
       //加载基本后更新

}

/*
在左边侧滑创建一个图表 , 需要传入图表的参数
 */
function createChartByParams(params)
{
    console.log("创建图表，参数:");
    console.log(params);
    $.post('charts2',params, function (data) {
         if(data.code===0) {

                 //将标题作为id
             var id = data.data.option.title[0].text.replace(' ','-');
             baseOptions.push(
                 {
                     id:id,
                     data:data.data
                 }
             );

             // vue 监听渲染完成还有，更新对应的图表
            chartlist.$nextTick(function () {
            console.log("更新数据后 渲染完成!,开始渲染图表..");
            console.log(data);
             var chart = echarts.init(document.getElementById(id));
             chart.setOption(data.data.option);

         });




            }
             else
             {
                    showJsonResult(data);
              }

    });
}

/*

选择指定数据源后的ajax更新
//1. 请求record记录，设置新建图表的可选字段
字段只有固定的
2.
*/

function selectDataSource(id)
{
    console.log("选择数据源:"+id);

    //字段
    recordid = id;



}
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

               var li = $('<li></li>',{

                   //设置点击事件为选择指定数据源，
                   onclick:'selectDataSource("'+ele.id+'");'
               });
               li.text(ele.id+ " "+ele.zsyear+ " "+ ele.status);

                select.append(li);
            });

            console.log(select);

             M.Dropdown.init(document.getElementById('datasource-trigger'));

        }
        else {
            console.log("获取数据源失败!!");
        }

    })


}



// 左边图表元素的点击时间 ，elementid 是图表id (显示是默认标题 ) 添加元素到列表,从baseOptions里找
function addChart(elementid)
{
    console.log('添加图表,id:'+elementid);
    console.log(report);

    baseOptions.forEach(function (value,index) {
       if(value.id===elementid)
       {
           console.log("找到对应id的option:");
           console.log(value);
            report.addElement(value.data);

       }
    });


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



//加载一开始的 模板
function loadBaseOption()
{

    //加载基本的图标
    $.get('options/zs?recordid=1',function(data){
        console.log('------------------------创建基本optons,--------------------------');
        console.log(data);
    //    data的键值是id和option
        for(var key in data.data)
        {
            console.log(key);
            console.log(data.data[key]);
            baseOptions.push({
                id:key,
                data:data.data[key]
            });
        }
              // vue 监听渲染完成还有，更新对应的图表
            chartlist.$nextTick(function () {
         for(var i = 0;i<baseOptions.length;i+=1) {
             console.log('初始化侧话图表:'+key);
             var chart = echarts.init(document.getElementById(baseOptions[i].id));
             chart.setOption(baseOptions[i].data.option);
         }
         });

    });


    // createChartByParams({
    //
    // });



}


//所有模板的options,侧滑那边的,结构为ReportItem结构
var baseOptions = [];


var report = new Report("report");
console.log("初始化..");
console.log(report);




loadDataSource();


// vue 绑定数据和标签
 var chartlist = new Vue({
        el:'#chartlist',
        data:{
            options:baseOptions
        }
    });
loadBaseOption();
//选择数据源后的可选字段,现在是招生的，暂时不会有变化，如果有其他数据，要动态切换，先保留
