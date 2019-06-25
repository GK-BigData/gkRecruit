// admin界面的js代码


//加载记录
function loadRecords()
{
    $.get("records",function(data){
        console.log(data);
        var records = data.data;
        //获取表格元素
        var table = $("#records");
        //清空元素
        table.empty();
    //    添加表头
        table.append("<thead><tr><th>id</th> <th>时间</th> <th>数据年份</th><th>状态</th> </tr></thead>")

        var tbody = document.createElement("tbody");
    //    添加行到body
        records.forEach(function(item,index){
            console.log(item);
            $(tbody).append("<tr>"+ "<td>"+item.id+ "</td>"
                + "<td>"+item.time+ "</td>"
                + "<td>"+item.zsyear+ "</td>"
                + "<td>"+item.status+ "</td>"
                +   "</tr>")

        });
        table.append(tbody)




    })


}


loadRecords();


