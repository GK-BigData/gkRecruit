// admin界面的js代码


//初始化模态框等
function initComponents()
{
    var info = $('#modal_info');
    //第一个参数为配置
    M.Modal.init(info,{
    //
    onOpenStart:function (modal,trigger) {
        console.log(trigger);
        console.log("on open start"+modal);
        console.log(modal);
        console.log(this);
        record_id = $(trigger).attr("data-id");
    //    ajax请求预览数据
        loadInfo(record_id);

    }
    });


}

function loadInfo(id)
{
    $('#progress_info').css('display','block');
    $.get('preview/'+id+'?type=html',function (data) {

        var table = $('#previewtable');
        table.empty();


        var a = table.append(data);
        console.log(data);
        $('#progress_info').css('display','none');

        console.log("加载信息完成:");
        console.log(data);

    })


}


//各种操作，loadRecords函数返回的html里的js调用
//通用请求成功函数
function actionSuccess(data)
{
    console.log(data);
    showJsonResult(data,'操作失败');
    loadRecords();
}
function actionError(data) {
       M.toast({html:"服务端响应失败:"+data});
}
//获取信息
function action_info(id)
{
    console.log("查看信息:"+id);

}
//删除数据
function action_delete(id) {
    console.log("删除数据:"+id);
    $.ajax({
        url:"records/"+id,
        method:"DELETE",
        success:actionSuccess,
        error:actionError
    })

}

function action_import(id)
{
    console.log("导入数据动作:"+id);

    window.open("setfield/"+id)


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
            console.log(data);
            console.log("上传成功");

             showJsonResult(data,'上传数据失败');

             $("#upload").removeClass("disabled");
            loadRecords();
            // if(data.code===0){}
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

initComponents();
