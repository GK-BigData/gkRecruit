// admin界面的js代码

//各种操作，loadRecords函数返回的html里的js调用

function action_info(id)
{

}


function action_import(id)
{
    console.log("导入数据动作:"+id);


}

//加载记录
function loadRecords()
{
    $.get("records_html",function(data){
        console.log(data);
        var records = data;
        //获取表格元素
        var table = $("#records");
        //清空元素
        table.empty();
    //    添加表头
        table.append("<thead><tr><th>id</th> <th>时间</th> <th>数据年份</th> <th>记录数</th> <th>状态</th><th>操作</th></tr></thead>");

    //     var tbody = document.createElement("tbody");
    // //    添加行到body
    //     records.forEach(function(item,index){
    //         console.log(item);
    //         $(tbody).append("<tr>"+ "<td>"+item.id+ "</td>"
    //             + "<td>"+item.time+ "</td>"
    //             + "<td>"+item.zsyear+ "</td>"
    //             + "<td>"+item.status+ "</td>"
    //             +   "</tr>")
    //
    //     });
        table.append(records);
        console.log("加载记录:");
        console.log(records);

    //    加载完的下拉,要手动初始
        console.log("初始化下拉框...");
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems);




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

    var year = $("#year option:selected").text();
    console.log("year:"+year);
    console.log(file);
    console.log(file.length);
    if(file.length===0)
    {

        console.log("请选择文件");
        return;
    }

    //上传解析时设置按钮成不用解析的
    $("#upload").addClass("disabled");

    formData.append("table",file[0]);
    formData.append("zsyear",year);

    console.log(formData);

    $.ajax({
        url:"upload",
        type:"POST",
        data:formData,
        contentType:false,
        processData:false,
        success:function (data) {
            console.log("上传成功");
             M.toast({html:"服务端响应成功:"+data.data});

             $("#upload").removeClass("disabled");
            
        },
        error:function()
        {
            console.log("上传失败");
            M.toast({html:"服务端响应失败"});
            $("#upload").removeClass("disabled");
        }

    })



}

loadRecords();


