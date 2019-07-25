function report() {
    $.ajax({
        url:'/report/data',
        data:{},
        type:'POST',
        dataType:'json',
        success:function (data) {
            console.log(data);
            for(var i =0;i<data.data.length;i+=1)
            {
                $('#report').append(data.data[i].title);

            }
            return data
        }
    })

}
