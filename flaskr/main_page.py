from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('main_page', __name__)


@bp.route('/')
@login_required
def index():
    db = get_db()
    # TODO: populate the dropdown with data
    year_dropdown_items = ['2022', '2023', '2024', '2025']
    month_dropdown_items = ['1','2','3','4','5','6','7','8','9','10','11','12']
    monthly_data = db.execute(
        'SELECT * FROM Transactions t JOIN Users u ON t.user_id = u.id'
    ).fetchall()
    return render_template('expenses/index.html', years=year_dropdown_items, months=month_dropdown_items)


@bp.route('/submit', methods=['POST'])
def submit():
    year_chosen = request.form.get("year_dropdown")
    month_chosen = request.form.get("month_dropdown")
    if (year_chosen == '2025' and month_chosen == '9'):
        flash("GÁCHI")
        pass
    else: 
        return 'GÁCHI'