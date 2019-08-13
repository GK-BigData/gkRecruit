function  Zs() {

}

//关闭按钮
Zs.prototype.disable=function (id) {

        $(id).addClass('disabled');
};

Zs.prototype.enable=function (id) {
        $(id).removeClass('disabled');
};

//显示隐藏元素
Zs.prototype.display=function(id){
        $(id).css('display','block');

};
Zs.prototype.hide=function(id){
        $(id).css('display','none');
};

//根据vale设置select 选择option的值,selectDom目标dom,values要选择的option的值
Zs.prototype.selectOption=function(selectDom,values){
        if(values===undefined)
        {
                console.log('选择select失败,没有指定values');
                console.log(selectDom);
                return;
        }
        console.log(values);
        //1.取消选择全部option,使用find而不是children因为有些option是在option group下面的
        var options = $(selectDom).find('option');


        //console.log(options);
        options.each(function(index,element){
                var item = $(element);

                console.log('处理:'+item.val());
                //在选中的值里有当前迭代的元素的话，就选中这个select
                if(values.indexOf(item.val())!==-1)
                {
                        console.log('选中:'+item.val());
                        item.attr('selected',true);
                }
                else
                        item.attr('selected',false);

        });

};