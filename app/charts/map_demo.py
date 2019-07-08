from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Funnel
def funnel_sort_ascending() :
    c = (
        Funnel()
        .add(
            "商品",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Sort（ascending）"))
    )
    for z in zip(Faker.choose(), Faker.values()):
        print(Faker.choose())
        print(Faker.values())
        print(z)
    return c

funnel_sort_ascending().render('map.html')
