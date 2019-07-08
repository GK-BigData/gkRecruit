

//值改变时 ，在后面显示出预览值,jquery查询到的所有select可以直接设置全部结果的change函数
$("select").change(function () {

   console.log("select 改变值了");

   var  select_element =  $(this);
   console.log(select_element);

    var id=select_element.attr('name');

    console.log(id);




});

//选择一列
function select_field(col)
{
    console.log("选择："+col+" 当前选择的id:"+nowSelectId);

    //nowSelectid就是输入框的Id
    $('#'+nowSelectId).val(col);
    field_modal.close();

    $('#'+nowSelectId+'-preview').html(preview[col].join(","));


}
//  设置选择后的预览信息,根据在setfield.html里设置的preview变量(模板渲染出来的js)
function update_preview()
{
//    获取所有字段选择下的input标签

}

//显示选择框,参数为数据库 字段名和 字段的名字
function showField(field,name)
{

    console.log("显示选择框:"+field+" name:"+name);

    console.log(field_modal);

    //保存当前选择的
    nowSelectId=field;

    field_modal.open();






}

//提交，填充数据到mysql
function submit() {

        $('#submit').addClass("disabled");
        $('#progress').css('display','block');

        $.ajax({

            url:"import",
            data:$("#fields").serialize(),
            type:"post",
            success:function (data) {
                $('#progress').css('display','none');
                $('#submit').removeClass("disabled");

                console.log("import success");
                 M.toast({html:"服务端响应成功:"+data.data});
                 if(data.code!==0)
                 {
                     showDialog("导入数据错误",data.data);
                 }
            },
            error:function (data) {
                $('#progress').css('display','none');
                $('#submit').removeClass("disabled");
                console.log("import fail");
                M.toast({html:"服务端响应失败"});

            }
        })

}

var field_modal=null;

//点击列表后选择的输入框的id
var nowSelectId = null;

document.addEventListener('DOMContentLoaded',function (evt) {

    var elements = $("#field_modal");

    field_modal = M.Modal.init(elements,{})[0];

    console.log("初始化modal成功...")

});