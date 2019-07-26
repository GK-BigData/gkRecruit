function report() {
    $.ajax({
        url:'/report/data',
        data:{},
        type:'GET',
        dataType:'json',
        success:function (data) {
            console.log(data);
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
                reportdata.push(data.data[i]);

            }
            return data
        }
    })

}
var reportdata = [];
var q = new Vue({
     el:'#report',
        data:{
            data:reportdata
        }
});
report();
