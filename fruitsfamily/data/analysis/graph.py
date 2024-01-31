import plotly.express as px
from fruitsfamily.data.analysis.db_analysis import DBAnalysis
from fruitsfamily.utils.file_utils import FileUtils
from fruitsfamily.configs.config import GRAPH_DIR


# import matplotlib.font_manager as fm
# import sys # debug
# sys.path.append(r'/Users/yyy/Documents/OZ_project/fruitsfamily/') # debug


class ShowGraph:
    def __init__(self):
        self.fig = None
        self.db_analysis = DBAnalysis()
        FileUtils.make_directories(GRAPH_DIR)

    def get_xy_axis(self, x_axis) -> tuple[list, list]:
        y = []
        if x_axis == "category":
            x = self.db_analysis.get_categories()
            for cate in x:
                count = self.db_analysis.get_count_by_category(cate)
                y.append(count)
        elif x_axis == "price":
            x, y = self.db_analysis.get_counts_by_price_range()
        else:
            x = []
        return x, y

    def get_graph_by_category(self) -> None:
        x, y = self.get_xy_axis("category")
        self.fig = px.bar(x=x, y=y, text_auto=True)
        self.fig.update_traces(textposition="outside")
        # self.show_graph()
        self.save_graph("category_bar")

    def get_graph_by_price(self) -> None:
        x, y = self.get_xy_axis("price")
        self.fig = px.bar(x=x, y=y, text_auto=True)
        self.fig.update_traces(textposition="outside")
        # self.show_graph()
        self.save_graph("price_bar")

    def show_graph(self) -> None:
        self.fig.show()

    def save_graph(self, title) -> None:
        self.fig.write_image(FileUtils.find_by_path(GRAPH_DIR) + f"/{title}.png")


# ShowGraph().get_graph_by_category()  # debug
# ShowGraph().get_graph_by_price()  # debug
