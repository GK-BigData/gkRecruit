// admin界面的js代码


//加载记录
function loadRecords()
{
    $.get("records",function(data){
        console.log(data);
        var records = data.data


    })


}


loadRecords();


