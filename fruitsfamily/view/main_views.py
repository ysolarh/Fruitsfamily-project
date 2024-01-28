from flask import Blueprint, render_template
from fruitsfamily.data.database.db_module import DatabaseModule
from fruitsfamily.data.database.db_query import SQL_ALL, SQL_CATE

bp = Blueprint('main', __name__, url_prefix='/')

db_module = DatabaseModule()
cur = db_module.cur
fruits_data = db_module.execute_all(SQL_ALL)
# fruits_data = db_module.execute_all(SQL_SEARCH_PRODUCT, "백팩")
# fruits_data = db_module.execute_all(SQL_SEARCH_PRODUCT, "NIKE")
category_data = db_module.execute_all(SQL_CATE)


@bp.route('/')
def index():
    return render_template('index.html', data_list=fruits_data, cate_list=category_data)