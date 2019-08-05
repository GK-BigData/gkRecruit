//options 编辑器

function OptionEditor(chart_dom)
{
    console.log('初始化Option编辑器....');



    this.dom = chart_dom;
    this.chart = echarts.getInstanceByDom(chart_dom);

    console.log('获取chart option...');
    console.log(chart.getOption());

    var self = this;
    console.log($('#option'));

    this.edit = new Vue(
        {
            el:'#option',
            data:{
                option:chart.getOption(),
                path:['配置'],
                values:['option']
            }
            ,methods:{

            },
            //计算属性，用来计算 path 的路径个数
            computed:{

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
                }

            }
        }
    );
    console.log(this.edit);

}

