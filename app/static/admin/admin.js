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


function upload() {

    console.log("上传文件.");



    var formData = new FormData();
    //上传的文件信息
    /*
    FileList {0: File, length: 1}
    0: FilelastModified: 1559701812061
    lastModifiedDate: Wed Jun 05 2019 10:30:12 GMT+0800 (中国标准时间)__proto__: Object
    name: "3.明星每月出现次数.png"
    size: 77142type: "image/png"webkitRelativePath: ""__proto__: Filelength: 1__proto__: FileList
     */
    var file = $("#uploadfile")[0].files;


    console.log(file);
    console.log(file.length);
    if(file.length===0)
    {
        console.log("请选择文件");
        return;
    }
    formData.append("table",file[0]);
    formData.append("zsyear","2018");
    console.log(formData);
    $.ajax({
        url:"upload",
        type:"POST",
        data:formData,
        contentType:false,
        processData:false,
        success:function (data) {
            console.log("上传成功")
            
        },
        error:function()
        {
            console.log("上传失败")
        }

    })



}

loadRecords();


