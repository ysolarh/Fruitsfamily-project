import numpy as np
import matplotlib.pyplot as plt
import mpld3

import sys

sys.path.append(r'/Users/yyy/Documents/OZ_project/fruitsfamily/')

from data.analysis.db_analysis import DBAnalysis


# import matplotlib.font_manager as fm


class ShowGraph:
    def __init__(self):
        self.db_analysis = DBAnalysis()
        plt.rc('font', family='AppleGothic')
        self.fig, self.ax = plt.subplots(1, 1, figsize=(10, 5))

    def show_by_category(self) -> None:
        categories = self.db_analysis.get_categories()
        count_category = self.db_analysis.get_count_category()
        x = np.arange(count_category)

        y = []
        for cate in categories:
            count = self.db_analysis.get_count_by_category(cate)
            y.append(count)

        self.ax.bar(x, y, align='center')
        # self.ax.set_xticks(x, categories)
        self.ax.set_xticklabels(categories)
        self.ax.set_xlabel('카테고리')
        self.ax.set_ylabel('개수')
        self.ax.set_title('카테고리 별 상품 개수')
        plt.show()

        # plt.bar(x, y, align='center', tick_label=categories)
        # plt.xticks(x, labels=categories)
        # plt.show()

        # m_html = mpld3.fig_to_html(self.fig, figid='graph-img')
        # with open("graph_show.html", "w") as f:
        #     f.write(m_html)


# print([f.name for f in fm.fontManager.ttflist])
ShowGraph().show_by_category()  # debug
