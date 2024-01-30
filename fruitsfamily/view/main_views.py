from flask import Blueprint, render_template, request, redirect, url_for

from fruitsfamily import Application
from fruitsfamily.data.analysis.graph2 import ShowGraph
from fruitsfamily.data.database.db_module import DatabaseModule
from fruitsfamily.data.database.db_query import SQL_ALL, SQL_CATE, SQL_SEARCH

bp = Blueprint('main', __name__, url_prefix='/')
db_module = DatabaseModule()

@bp.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    fruits_data = db_module.execute_all(SQL_SEARCH, keyword, keyword)
    category_data = db_module.execute_all(SQL_CATE)
    # return render_template('index.html', data_list=fruits_data)
    return render_template('index.html', data_list=fruits_data, cate_list=category_data)

@bp.route('/update', methods=['GET'])
def update():
    Application().run() # update할때 작동시킬것
    ShowGraph().get_graph_by_category()  # debug
    ShowGraph().get_graph_by_price()  # debug
    category_data = db_module.execute_all(SQL_CATE)
    fruits_data = db_module.execute_all(SQL_ALL)
    render_template('index.html', data_list=fruits_data, cate_list=category_data)
    return redirect(url_for('main.index'))

@bp.route('/')
def index():
    # cur = db_module.cur
    category_data = db_module.execute_all(SQL_CATE)
    fruits_data = db_module.execute_all(SQL_ALL)
    return render_template('index.html', data_list=fruits_data, cate_list=category_data)