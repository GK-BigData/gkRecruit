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