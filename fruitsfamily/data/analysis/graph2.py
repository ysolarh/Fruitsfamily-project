import plotly.express as px
from fruitsfamily.data.analysis.db_analysis import DBAnalysis
from fruitsfamily.utils.file_utils import FileUtils
from fruitsfamily.configs.config import GRAPH_DIR

# import matplotlib.font_manager as fm
# import sys # debug
# sys.path.append(r'/Users/yyy/Documents/OZ_project/fruitsfamily/') # debug



class ShowGraph:
    def __init__(self):
        self.db_analysis = DBAnalysis()
        FileUtils.make_directories(GRAPH_DIR)


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
        # fig.show()
        fig.write_image(FileUtils.find_by_path(GRAPH_DIR) + "/bar.png")

    # def put_graph_in_html(self):


# ShowGraph().show_bar_graph()  # debug
