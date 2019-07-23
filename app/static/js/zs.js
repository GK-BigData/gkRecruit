function  Zs() {

}

//关闭按钮
Zs.prototype.disable=function (id) {

        $(id).addClass('disabled');
};

Zs.prototype.enable=function (id) {
        $(id).removeClass('disabled');
};