//简易修改,chart_dom, echart所在的dom元素
function EChartEditor(chart_dom){

        console.log('初始化EChartEditor..');
        if(chart_dom===undefined)
        {
            console.log('严重错误,Echart dom无效');
            return;
        }
        console.log(chart_dom);

        this.dom = chart_dom;

        this.chart = echarts.getInstanceByDom(chart_dom);

        console.log(chart.getOption());
        // 获取框高的元素

        var self = this;

        this.edit = new Vue({
        el:'#chartEdit',
        data:{
            chart:{
                //初始化为当前dom的长宽
                width:self.dom.style.width.replace('px',''),
                height:self.dom.style.height.replace('px','')

            },
            option:chart.getOption()
        },
            methods:{
                //对应
                changeSize:function(what)
                {
                    console.log(this.chart.width + " height:"+this.chart.height);
                //    更新echart宽高
                    self.dom.style.width=this.chart.height+'px';
                    self.dom.style.height=this.chart.height+'px';
                    console.log(self.dom);
                    self.chart.resize();

                },
                changeOption:function(){
                    self.chart.setOption(this.option);
                },
                input:function()
                {
                   // console.log('input...');
                }

            }

    });
}

