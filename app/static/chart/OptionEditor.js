//options 编辑器

function OptionEditor( )
{
    console.log('初始化Option编辑器....');







}

OptionEditor.prototype.loadVue=function()
{
    var self = this;
     this.edit = new Vue(
        {
            el:'#option',
            data:{
                option:self.chart.getOption(),
                //用来显示上面的导航的中文
                path:['配置'],
                //键列表，用来定位对象
                values:['option']
            }
            ,methods:{
    //根据path当前的对象
                nowObject:function(){
                    console.log('计算object');

                    var temp = this.option;
                    this.values.forEach(function(value){
                        if(value!=='option')
                       temp =  temp[value];
                    });
                    console.log(temp);
                    return temp;
                },
                //点击上面的条，传进来的是一个位移，打开开始到这个位移的路径
                enterObjectByOffset:function(index){
                    console.log('通过下标进入对象，下标:'+index+' 处理后的路径');
                    //删除位移后的,假设长度为3,点击里第二个元素,index=1 , 就是(index+1,le-index-1)=1,1
                    this.path.splice(index+1,this.path.length-index-1);
                    this.values.splice(index+1,this.values.length-index-1);
                    console.log(this.path);
                    console.log(this.values);
                },
                //对象点击事件
                enterObject:function(key)
                {
                    console.log('进入对象:'+key);
                    this.path.push(key);
                    this.values.push(key);

                },
                changeOption:function () {

                    console.log('Option 更新 Option.....:');
                    console.log(self.chart);
                    console.log(this.option);
                    //输入值改变后监听，更新option
                    self.chart.setOption(this.option);

                }
            },
            //计算属性，用来计算 path 的路径个数
            computed:{


                //可选的object类型的对象
                getObjects:function(){

                    var object = this.nowObject();
                    console.log('getObjects........,object:');
                    console.log(object);
                    var keys = [];
                    for(var key in object)
                    {
                        var type = typeof object[key];
                        console.log('遍历对象:'+key+" 类型:"+type);
                        if(type==='object')
                        {
                            keys.push(key);
                        }

                    }

                    return keys;
                },
                //获取编辑的东西,返回对象和键值
                getEditors:function(){
                    var keys = [];
                    var object = this.nowObject();
                    for(var key in object)
                    {
                        var type = typeof object[key];
                        var input_type='text';
                        if(type!=='object')
                        {
                            if(type==='boolean')input_type='checkbox';
                            console.log('可编辑类型:'+type+" 输入类型:"+input_type);
                            //要传入对象和key，让前端根据object，直接传值给v-mdoel是接受不到的
                            keys.push({
                                key:key,
                                object:object,
                                input_type:input_type
                            });
                        }

                    }
                    this.$nextTick(function () {
                        console.log('渲染完成,更新text label....');
                        //渲染完成,更新text label
                        M.updateTextFields();
                    });
                    return keys;
                },

                //可选数组的对象,对于有多个
                getArrayOffset:function(){

                }

            }
        }
    );

};


OptionEditor.prototype.setChartByDom=function (dom) {


    if(dom===undefined){
        console.log('option 编辑,切换图表dom失败')
    }
    console.log('OptionEdit 设置dom:');
    console.log(dom);

    this.dom = dom;
    this.chart = echarts.getInstanceByDom(dom);


    if(this.edit===undefined)this.loadVue();

    this.edit.path=['Option'];
    this.edit.values=['option'];
    this.edit.option = this.chart.getOption();


};