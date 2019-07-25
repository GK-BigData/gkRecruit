from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Map, Radar, PictorialBar, Funnel
from pyecharts.globals import ThemeType, SymbolType
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts


class All_Picture():

    def __init__(self,fields, title, subtitle='', y_name='', x_name=''):
        # 加入字段为了用来指定stack时的值
        self.fields=fields
        self.y_name = y_name
        self.x_name = x_name
        self.title = title
        self.subtitle = subtitle
        self.init_opts = opts.InitOpts(theme=ThemeType.LIGHT)
        self.logo = [
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

    def bar_picture(self, series_names, bar_xdata, bar_ydatas,stack=False):
        print('饼图,数组:')
        print(bar_xdata)
        b = (
            Bar(init_opts=self.init_opts)
                .add_xaxis(bar_xdata)
                .set_global_opts(
                title_opts=opts.TitleOpts(title=self.title, subtitle=self.subtitle),
                # 显示下载等按钮
                toolbox_opts=opts.ToolboxOpts(),
                legend_opts=opts.LegendOpts(is_show=True),

                # 设置y轴名称和value单位
                yaxis_opts=opts.AxisOpts( axislabel_opts=opts.LabelOpts(formatter="{value}")),
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=27)),

                # 设置logo
                graphic_opts=self.logo
            )
                # 是否翻转
               # .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="inside"))

        )

        for name, ydata in zip(series_names, bar_ydatas):
            # 堆叠暂时使用最后一个字段的名字来堆叠
            if stack:
                b.add_yaxis(name,ydata,stack=self.fields[-1])
            else:
                b.add_yaxis(name, ydata)
        print(b)
        return b

    def rose_picture(self,series_names, rose_xdata, rose_ydatas):
        print(rose_ydatas)
        print(series_names)
        p = (
            Pie(init_opts=self.init_opts)

                .set_global_opts(title_opts=opts.TitleOpts(title=self.title, subtitle=self.subtitle),
                                 # 调整位置
                                 # legend_opts=opts.LegendOpts(pos_left="15%"),

                                 # 添加logo
                                 graphic_opts=self.logo
                                 )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
        )
        for series_name, item_x, item_y in zip(series_names, rose_xdata, rose_ydatas):
            print('add series:', series_name)
            p.add(series_name, [list(z) for z in zip(item_x, item_y)],  radius=["30%", "75%"],
                     center=["25%", "50%"],
                     rosetype="radius",
                     label_opts=opts.LabelOpts(is_show=True))


        return p

    def rose_picture_man_women(self, man_name, women_name, man_data, women_data):
        p = (
            Pie(init_opts=self.init_opts)
                .add("男",
                     [list(p) for p in zip(man_name, man_data)],
                     radius=["30%", "75%"],
                     center=["25%", "50%"],
                     rosetype="radius",
                     label_opts=opts.LabelOpts(is_show=False),
                     )
                .add(
                "女",
                [list(z) for z in zip(women_name, women_data)],
                radius=["30%", "75%"],
                center=["75%", "50%"],
                rosetype="area",
            )

                .set_global_opts(title_opts=opts.TitleOpts(title=self.title, subtitle=self.subtitle),
                                 # 调整位置
                                 # legend_opts=opts.LegendOpts(pos_left="15%"),

                                 # 添加logo
                                 graphic_opts=self.logo
                                 )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
        )
        return p

    def pie_picture(self,series_names, x, y):
        print("系列")
        print(series_names)
        print(x)
        print(y)
        p = (
            Pie(init_opts=self.init_opts)
                .set_global_opts(title_opts=opts.TitleOpts(title=self.title, subtitle=self.subtitle),
                                 # 添加logo
                                 graphic_opts=self.logo
                                 )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
        )
        # 传进来的,x,y都是列表的列表，每个是一个series
        for series_name ,item_x , item_y in zip(series_names, x,y):
            print('add series:',series_name)
            p.add(series_name, [list(z) for z in zip(item_x, item_y)])
        return p

    # 广东地图
    def guangdong_map_picture(self, x_data, y_data):
        g = (
            Map(init_opts=self.init_opts)
                .add("标示，修改这里", [list(z) for z in zip(x_data, y_data)], "广东")
                .set_global_opts(title_opts=opts.TitleOpts(title=self.title, subtitle=self.subtitle),
                                 # 分段类型
                                 visualmap_opts=opts.VisualMapOpts(max_=1000, is_piecewise=True),
                                 # 添加logo
                                 graphic_opts=self.logo
                                 )

        )

        # 返回option
        return g

    # 中国地图
    def china_map_picture(self, x_data, y_data):
        print(x_data)
        print(y_data)
        c = (
            Map(init_opts=self.init_opts)
                .add("地理:人数", [list(z) for z in zip(x_data, y_data)], "china")
                .set_global_opts(title_opts=opts.TitleOpts(title=self.title, subtitle=self.subtitle),
                                 # 分段类型
                                 visualmap_opts=opts.VisualMapOpts(max_=200)

                                 # 添加logo
                                 # graphic_opts=self.logo
                                 )

        )

        # 返回option
        return c

    # 雷达图--各个学院男女比例占比
    def radar_picture(self, seriesname: list, values: list, schemanames):
        #
        # maxvalue = 0
        # for value in value1+value2:
        #     if value>maxvalue:
        #         maxvalue=value

        '''
        v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
        v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
        '''

        schema = []
        print("schenames:", schemanames)
        for index, name in enumerate(schemanames):

            maxvalue = -1
            all = []
            # 第一个循环遍历所有series
            for i in range(0, len(seriesname)):

                if values[i][index] > maxvalue:
                    maxvalue = values[i][index]
                all.append(values[i][index])
            schema.append(opts.RadarIndicatorItem(name=name, max_=maxvalue))
            print(all)
        r = (Radar(init_opts=self.init_opts)
             .add_schema(
            schema=schema
        )
             .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
             .set_global_opts(title_opts=opts.TitleOpts(title=self.title, subtitle=self.subtitle),
                              # 添加logo
                              graphic_opts=self.logo
                              ))
        for name, value in zip(seriesname, values):
            r.add(name, [value])

        return r

    # 表格
    def table_picture(self, headers, data):
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
        headers = [""]
        data = [
            []
        ]
        table = (
            Table()
                .add(headers=headers, rows=data)
                .set_global_opts(title_opts=ComponentTitleOpts(title=self.title, subtitle=self.subtitle),
                                 # 添加logo
                                 graphic_opts=self.logo
                                 )
        )

        return table

    def pictorialbar_base(self, x_data, y_data):
        c = (
            PictorialBar()
                .add_xaxis(x_data)
                .add_yaxis(
                "",
                y_data,
                label_opts=opts.LabelOpts(is_show=False),
                symbol_size=22,
                symbol_repeat="fixed",
                symbol_offset=[0, -5],
                is_symbol_clip=True,
                symbol=SymbolType.ROUND_RECT,
            )
                .reversal_axis()
                .set_global_opts(
                title_opts=opts.TitleOpts(title="各学院人数占比"),
                xaxis_opts=opts.AxisOpts(is_show=False),
                yaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(opacity=0)
                    ),
                ),
            )
        )
        return c

    def funnel_sort_ascending(self,series_name,  x_data, y_data):
        print('funel:',x_data,y_data)
        c = (
            Funnel()
                .add(
                series_name[0],
                [list(z) for z in zip(x_data, y_data)],
                # sort_="ascending",
                label_opts=opts.LabelOpts(position="inside"),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title=self.title))
        )

        return c
