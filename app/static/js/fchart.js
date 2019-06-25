/**
@Project:   
@Date:      2019/5/17 下午3:51

ajax和echart封装的一些函数

*/


function errorTip(msg)
{
    console.log("eror msg:"+msg)
    M.toast({html:msg,});
}

//初始化图标
function initChart(id)
{
    console.log("init chart,:")
    console.log(id)
    console.log(document.getElementById(id))
    return echarts.init(document.getElementById(id))

}

//通用请求图表数据和设置图表
function ajaxChart(url,chart,callback,ispost,data)
{
    if(ispost)
    {
    $.post(url,data,function(data){
            if(data.code!=1)
            {
            errorTip("错误代码:"+data.code+" "+data.data);
            return;
            }


//            错误代码就不传了
            callback(chart,data.data)

    });
    }
    else
    $.get(url,function(data){
            if(data.code!=1)
            {
            errorTip("错误代码:"+data.code+" "+data.data);
            return;
            }


//            错误代码就不传了
            callback(chart,data.data)

    });

}