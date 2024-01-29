from flask import Blueprint, render_template, request
from fruitsfamily.data.database.db_module import DatabaseModule
from fruitsfamily.data.database.db_query import SQL_ALL, SQL_CATE

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    db_module = DatabaseModule()
    # cur = db_module.cur
    category_data = db_module.execute_all(SQL_CATE)
    fruits_data = db_module.execute_all(SQL_ALL)
    # fruits_data = db_module.execute_all(SQL_SEARCH_PRODUCT, "백팩")
    # fruits_data = db_module.execute_all(SQL_SEARCH_PRODUCT, "NIKE")
    return render_template('index.html', data_list=fruits_data, cate_list=category_data)