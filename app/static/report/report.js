function report() {
    $.ajax({
        url:'/report/data',
        data:{},
        type:'GET',
        dataType:'json',
        success:function (data) {
            console.log(data);
            //先清空全部数据
            reports.splice(0,reports.length);
            for(var i =0;i<data.data.length;i+=1)
            {
                // var li = $('<li ></li>',{
                //
                // });
                // var a = $('<a></a>',{href:'http://baidu.com/'+data.data[i].id});
                // li.append(a);
                // li.text(data.data[i].title);
                //
                // $('#report').append(li);
                console.log('添加元素:');
                reports.push(data.data[i]);

            }
            return data
        }
    })

}

//点击创建按钮后的
function createReport()
{
    var select_temp = M.FormSelect.init(document.getElementById('report_template'));
    var select_record = M.FormSelect.init(document.getElementById('report_record'));

    var template = select_temp.getSelectedValues()[0];
    var recordid = select_record.getSelectedValues()[0];

    var title = $('#report_title').val();



    $.ajax({
        url:'reports',
        type:'POST',
        data:{
            'title':title,
            'template':template,
            'recordid':recordid

        },
        dataType:"json",
        success:function (data,status) {
            console.log('创建报告，服务器返回成功!');
            console.log(data);
            report();
        },
        error:function (data) {
            console.log('更新错误!');
            console.log(data);
        }

    });


}
function addReport()
{

modal_create_report.open();

}

function loadVue()
{
//    注册Vue组件

    Vue.component('report-item',{
        props:['report'],
        template: `
        <div class="card col s3" style="margin-left: 20px;">
        <div class="card-title">{{ report.title }}</div>
        <div class="card-content">时间 {{ report.time }}<br>balabala</div>
        <div class="card-action">
        <a href="#" v-on:click="$emit('edit',report.id)">编辑？？/</a>
        <a href="#" v-on:click="$emit('delete_report',report.id)">删除..</a>
</div>
        
</div>
        `
    });


    new Vue({
        el:'#reports',
        data:{
            reports:reports
        },
        //函数
        methods:{
            edit:function (id) {
                console.log("编辑报告:"+id);

                window.open("../main/"+id)
            },
            delete_report:function(id){

                zsDialog.setParam('标题','删除?',function(){
                    console.log('点击了删除');
                //    发送请求删除
                    $.ajax({
                        url:'reports/'+id,
                        method:'delete',
                        success:function (data) {
                            console.log('删除成功');
                            report()

                        },
                        error:function (data) {
                            console.log('删除失败');
                            console.log(data);

                        }
                    })

                });
                zsDialog.show();
            }
        }
    });



    modal_create_report =  M.Modal.init(document.getElementById('modal-create-report'),{});

//    模板选择select
    M.FormSelect.init(document.getElementById('report_template'))

}


var reports=[];
var modal_create_report;

var create_report = {
};

report();
loadVue();