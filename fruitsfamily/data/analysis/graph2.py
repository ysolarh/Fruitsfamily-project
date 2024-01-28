import plotly.express as px

# import sys # debug

# sys.path.append(r'/Users/yyy/Documents/OZ_project/fruitsfamily/') # debug

from fruitsfamily.data.analysis.db_analysis import DBAnalysis


# import matplotlib.font_manager as fm


class ShowGraph:
    def __init__(self):
        self.db_analysis = DBAnalysis()

    def get_xy_axis(self) -> tuple[list, list]:
        categories = self.db_analysis.get_categories()
        # count_category = self.db_analysis.get_count_category()

        y = []
        for cate in categories:
            count = self.db_analysis.get_count_by_category(cate)
            y.append(count)

        return categories, y

    def show_bar_graph(self):
        x, y = self.get_xy_axis()
        fig = px.bar(x=x, y=y)
        fig.show()

    # def put_graph_in_html(self):


ShowGraph().show_bar_graph()  # debug
