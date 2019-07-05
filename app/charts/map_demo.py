from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Map


def bar_chart() -> Map:
    c = (
        Map()
            .add("商家A", [list(z) for z in zip(Faker.guangdong_city, Faker.values())], "广东")
            .set_global_opts(title_opts=opts.TitleOpts(title="map-demo"),
                             visualmap_opts=opts.VisualMapOpts(max_=200)
                             )

    )
    for z in zip(Faker.guangdong_city, Faker.values()):
        print(list(z))

    return c
bar_chart().render('map.html')
