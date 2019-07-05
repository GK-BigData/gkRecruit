
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