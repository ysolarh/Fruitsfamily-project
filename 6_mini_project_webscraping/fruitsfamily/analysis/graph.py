import numpy as np
import matplotlib.pyplot as plt

# import sys

# sys.path.append(r'fruitsfamily/analysis/db_analysis.py')
from analysis.db_analysis import DBAnalysis
# import matplotlib.font_manager as fm


class ShowGraph:
    def __init__(self):
        self.db_analysis = DBAnalysis()
        plt.rc('font', family='AppleGothic')

    def show_by_category(self) -> None:
        categories = self.db_analysis.get_categories()
        count_category = self.db_analysis.get_count_category()
        print(count_category)
        x = np.arange(count_category)

        count_by_category = []
        for cate in categories:
            count = self.db_analysis.get_count_by_category(cate)
            count_by_category.append(count)
        plt.bar(x, count_by_category, align='center', tick_label=categories)
        #plt.xticks(x, labels=categories)
        plt.show()


# print([f.name for f in fm.fontManager.ttflist])
ShowGraph().show_by_category()  # debug
