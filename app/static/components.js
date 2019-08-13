// Vue组件

//注册组件
 // 自定义组件的v-model
Vue.component('percent-range',{
            //提供的属性,这里的值可以在template里使用
            //props:['title','min','max'],
            props:{
                value:{
                },
              title:String,
              min:{
                  default:0
              }  ,
                max:{
                  default: 100
                }
            },
            data:function(){
                //console.log(this.title);
                //console.log(this.value);
                //确保为字符串,不然,endsWith函数就用不了了
                this.pvalue=this.value+'';
                //根据输入的value prop来设置百分比是否选择这些
                if (this.pvalue.endsWith('%'))
                    return {
                    ispercent:true,
                  //初始值设置为prop的值g,pvalue表示自定义组件的value的值
                    pvalue: parseInt( this.value.replace('%',''))
                };
                    else
                return {
                    ispercent:false,
                  //初始值设置为prop的值g,pvalue表示自定义组件的value的值
                    pvalue: parseInt( this.value)
                }
            },
            methods:{
                //获取值的文字，因为有百分比，所以提供一个函数
                getValue:function ()
                {
                    if(this.ispercent)return this.pvalue+"%";
                    else return this.pvalue;
                },
                //值改变
                change:function(v)
                {
                    this.$emit('change',this.getValue());
                }
                ,
                input:function (v) {
                    //可以用参数的v或者data里的value，因为那个value和input ranage是绑定的
                    //这里要处理百分比，所以用value
                 //console.log('range 输入了:'+this.getValue());
                 //父组件在这里用里v-model的话，触发这个组件的input方法，让父组件接受
                 this.$emit('input',this.getValue());
                }
            },
            template:'<div>\n' +
                '    <label> <span>{{ title }}</span><span> {{ getValue() }} </span>  <input v-on:change="change()" v-on:input="input($event.target.value)" v-model="pvalue" style="width:50%" type="range"/> </label>\n' +
                '    <label><input v-model="ispercent" type="checkbox" /> <span>使用百分比</span></label>\n' +
                '    </div>'

        });



Vue.component('select-range',{

    props:{
        title:{

        },
        //option值
        values:{

        },
        //option显示的
        names:{}
    },
    data:function () {
        
    }

    ,
    template:'    <div class="row">\n' +
        '    <div class="input-field s8 inline"><input id="a" type="text"/><label >{{title}}</label></div>\n' +
        '    <div class="input-field s4 inline"><select class="browser-default">\n' +
        '        <option value="android">Android</option>\n' +
        '        <option value="linux">Linux</option>\n' +
        '        <option value="win">windows</option>\n' +
        '    </select>\n' +
        '\n' +
        '    </div>'

});
