// 通用初始化 Material的各个组件
document.addEventListener('DOMContentLoaded',function (evt) {
    var elements = document.querySelectorAll("select");

    var selects = M.FormSelect.init(elements);

    //----------初始化modal 模态框
//    var modal_elements = document.querySelectorAll(".modal");
  //  var modal = M.Modal.init(modal_elements);

});

//对话框封装
function ZsDialog(){

    this.modal = M.Modal.init(document.getElementById('confirm-modal'));
    this.title = $('#confirm-title');
    this.content = $('#confirm-content');
    this.yes = $('#confirm-yes');
}

//设置对话框显示的参数,标题，信息,确定后的回调函数
ZsDialog.prototype.setParam=function(title,content,callback){
        this.title.text(title);
        this.content.text(content);
        this.yes.click(callback);
};

ZsDialog.prototype.show=function () {
    this.modal.open();
};