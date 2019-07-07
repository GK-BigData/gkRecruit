

//值改变时 ，在后面显示出预览值,jquery查询到的所有select可以直接设置全部结果的change函数
$("select").change(function () {

   console.log("select 改变值了");

   var  select_element =  $(this);
   console.log(select_element);

    var id=select_element.attr('name');

    console.log(id);




});
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
            },
            error:function (data) {
                $('#progress').css('display','none');
                $('#submit').removeClass("disabled");
                console.log("import fail");
                M.toast({html:"服务端响应失败"});
            }
        })

}