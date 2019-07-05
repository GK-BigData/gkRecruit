from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Map, Radar
from pyecharts.globals import ThemeType
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts


class All_Picture():
    def __init__(self,title,subtitle=''):
        self.title=title
        self.subtitle=subtitle
        self.init_opts = opts.InitOpts(theme=ThemeType.LIGHT)
        self.logo=[
                                 opts.GraphicImage(
                                     graphic_item=opts.GraphicItem(
                                         id_='logo',
                                         right=20,
                                         top=20,
                                         z=-10,
                                         bounding="raw",
                                         origin=[75, 75]
                                     ),
                                     graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                                         image="logo.png",
                                         width=110,
                                         height=110,
                                         opacity=0.4

                                     )
                                 )
                             ]

    def bar_picture(self,bar_xdata,bar_ydata):
        b = (
            Bar(init_opts=self.init_opts)
            .add_xaxis(bar_xdata)
            .add_yaxis("d", bar_ydata)

            .set_global_opts(
                title_opts=opts.TitleOpts(title=self.title,subtitle="副标题"),
                #显示下载等按钮
                toolbox_opts=opts.ToolboxOpts(),
                legend_opts=opts.LegendOpts(is_show=False),

                #设置y轴名称和value单位
                yaxis_opts=opts.AxisOpts(name="y轴名称",axislabel_opts=opts.LabelOpts(formatter="{value}/单位")),

                #设置x轴名称
                xaxis_opts=opts.AxisOpts(name="x轴名称"),

                #设置logo
                graphic_opts=self.logo
            )
            # 是否翻转
            .reversal_axis()
            .set_series_opts(
                # 翻转后的位置
                label_opts=opts.LabelOpts(position="right"),
                markpoint_opts=opts.MarkPointOpts(
                    data=[
                        opts.MarkPointItem(type_="max",name="最大值"),
                        opts.MarkPointItem(type_="min", name="最小值"),
                        opts.MarkPointItem(type_="average", name="平均值"),
                    ]
                )
            )
        )
        print(b)

        return b.dump_options()

    def rose_picture(self,x_data,y_data):
        p=(
            Pie(init_opts=self.init_opts)
            .add("",
                 [list(p) for p in zip(x_data,y_data)],
                 radius=["30%", "75%"],
                 center=["25%", "50%"],
                 rosetype="radius",
                 label_opts=opts.LabelOpts(is_show=False),
                 )
                .add(
                "",
                [list(z) for z in zip(x_data, y_data)],
                radius=["30%", "75%"],
                center=["75%", "50%"],
                rosetype="area",
            )

            .set_global_opts(title_opts=opts.TitleOpts(title="修改这里，标题"),
                             #调整位置
                             #legend_opts=opts.LegendOpts(pos_left="15%"),

                             # 添加logo
                             graphic_opts=self.logo
                             )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
        )
        return p.dump_options()

    def pie_picture(self,x_data,y_data):
        p = (
            Pie(init_opts=self.init_opts)
                .add("",[list(p) for p in zip(x_data, y_data)])
                .set_global_opts(title_opts=opts.TitleOpts(title="修改这里，标题"),
                                 #添加logo
                                 graphic_opts=self.logo
                                 )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
        )
        return p.dump_options()

    #广东地图
    def guangdong_map_picture(self,x_data,y_data):
        g = (
            Map(init_opts=self.init_opts)
                .add("标示，修改这里", [list(z) for z in zip(x_data, y_data)], "广东")
                .set_global_opts(title_opts=opts.TitleOpts(title="修改这里,标题"),
                                 #分段类型
                                 visualmap_opts=opts.VisualMapOpts(max_=1000,is_piecewise=True),
                                 # 添加logo
                                 graphic_opts=self.logo
                                 )

        )

        #返回option
        return g.dump_options()

    #中国地图
    def china_map_picture(self,x_data,y_data):
        c = (
            Map(init_opts=self.init_opts)
                .add("标示，修改这里", [list(z) for z in zip(x_data, y_data)], "china")
                .set_global_opts(title_opts=opts.TitleOpts(title="修改这里,标题"),
                                 # 分段类型
                                 visualmap_opts=opts.VisualMapOpts(max_=1000, is_piecewise=True),

                                 # 添加logo
                                 graphic_opts=self.logo
                                 )

        )

        # 返回option
        return c.dump_options()

    #雷达图--各个学院男女比例占比
    def radar_picture(self,value1,value2,schemanames):

        #各个学院男生人数占比
        v1=list(value1)

        #各个学院女生人数占比
        v2=list(value2)

        '''
        v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
        v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
        '''
        schema=[]
        for name in schemanames:
            schema.append(opts.RadarIndicatorItem(name=name,max_=3000))
        r=(
            Radar(init_opts=self.init_opts)
            .add_schema(
                schema=schema
            )
            .add("男",v1)
            .add("女",v2)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="主标题-修改这里"),
                             # 添加logo
                             graphic_opts=self.logo
                             )
        )

        return r.dump_options()


    #表格
    def table_picture(self,headers,data):
        '''
        数据类似
         headers = ["City name", "Area", "Population", "Annual Rainfall"]
        data = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
        '''
        headers=[""]
        data=[
            []
        ]
        table=(
            Table()
            .add(headers=headers,rows=data)
            .set_global_opts(title_opts=ComponentTitleOpts(title="主标题",subtitle="副标题"),
                             # 添加logo
                             graphic_opts=self.logo
                             )
        )

        return table



if __name__=='__main__':
    AP=All_Picture()

