from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType


class All_Picture():
    def __init__(self):
        self.init_opts = opts.InitOpts(theme=ThemeType.LIGHT)

    def getchart(self,db,zyear,chartid):
        pass
        self.db = db

    def bar_picture(self,bar_xdata,bar_ydata):
        bar_xdata=bar_xdata
        bar_ydata=bar_ydata

        b = (
            Bar(init_opts=self.init_opts)
            .add_xaxis(bar_xdata)
            .add_yaxis("图形实例",bar_ydata)

            .set_global_opts(
                title_opts=opts.TitleOpts(title="主标题",subtitle="副标题"),
                #显示下载等按钮
                toolbox_opts=opts.ToolboxOpts(),
                legend_opts=opts.LegendOpts(is_show=False),

                #设置y轴名称和value单位
                yaxis_opts=opts.AxisOpts(name="y轴",axislabel_opts=opts.LabelOpts(formatter="{value}/单位")),

                #设置x轴名称
                xaxis_opts=opts.AxisOpts(name="x轴"),

                #设置logo
                graphic_opts=[
                    opts.GraphicImage(
                        graphic_item=opts.GraphicItem(
                            id_='logo',
                            right=20,
                            top=20,
                            z=-10,
                            bounding="raw",
                            origin=[75,75]
                        ),
                        graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                            image="http://127.0.0.1:5000/static/main/logo.png",
                            width=110,
                            height=110,
                            opacity=0.4

                        )
                    )
                ]


            )
            # 是否翻转
            # .reversal_axis()
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


if __name__=='__main__':
    AP=All_Picture()
    test = AP.bar_picture([1,2],[2,4])
    print(test)
    print(type(test))
