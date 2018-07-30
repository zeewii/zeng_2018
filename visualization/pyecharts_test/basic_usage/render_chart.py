#coding=utf-8
from pyecharts import Bar, Pie, Page, Line
from pyecharts.engine import create_default_environment

def create_charts():
    page = Page()

    #饼形图
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    chart = Pie("饼图示例1")
    chart.add("", attr, v1, is_label_show=True)
    #chart.render()
    page.add(chart)

    #1.第一个示例
    bar = Bar("我的第一个图表1", "这里是副标题")
    #主要方法，用于添加图表的数据和设置各种配置项
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], \
        [5, 20, 36, 10, 75, 90])
    # 该行只为了打印配置项，方便调试时使用
    bar.print_echarts_options()
    # 生成本地 HTML 文件
    #默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，
    # 如 render(r"e:\my_first_chart.html")，文件用浏览器打开。
    bar.render(r'我的第一个图表.html')
    #使用Page类，将图表加入到对象中
    page.add(bar)



    #2.如果想要提供更多实用工具按钮，请在 add() 中设置 is_more_utils 为 True
    bar = Bar("我的第一个图表2", "这里是副标题")
    bar.add("服装",
        ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],
        is_more_utils=True)
    #bar.render()
    page.add(bar)




    #3.使用主题
    bar = Bar("我的第一个图表3", "这里是副标题")
    bar.use_theme('dark')
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], \
         [5, 20, 36, 10, 75, 90])
    #bar.render()
    page.add(bar)



    #4.使用 pyecharts-snapshot 插件--直接保存为图片，
    # 文件结尾可以为 svg/jpeg/png/pdf/gif。
    # 请注意，svg 文件需要你在初始化 bar 的时候设置 renderer='svg'。
    bar = Bar("我的第一个图表4", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    bar.render(path=r'我的第一个图表.gif')
    #page.add(bar)



    #5.多次显示图表
    bar = Bar("我的第一个图表5", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    line = Line("我的第一个图表", "这里是副标题")
    line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    env = create_default_environment("html")
    #  为渲染创建一个默认配置环境
    # create_default_environment(filet_ype)
    # file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'
    env.render_chart_to_file(bar, path='bar.html')
    env.render_chart_to_file(line, path='line.html')



    return page










create_charts().render()









