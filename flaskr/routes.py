from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from .helpers import allowed_file, save_file

bp = Blueprint('main', __name__)


@bp.route('/')
@login_required
def index():
    db = get_db()
    # TODO: populate the dropdown with data
    year_dropdown_items = ['2022', '2023', '2024', '2025']
    month_dropdown_items = ['1','2','3','4','5','6','7','8','9','10','11','12']
    # monthly_data = db.execute(
    #     'SELECT * FROM Transactions t JOIN Users u ON t.user_id = u.id'
    # ).fetchall()
    return render_template('expenses/index.html', years=year_dropdown_items, months=month_dropdown_items)


@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = save_file(file)
            flash(f'File {filename} uploaded successfully!')
            return redirect(url_for('main.upload'))
        else:
            flash('Invalid file type! Allowed types: ' + ', '.join(current_app.config['ALLOWED_EXTENSIONS']))
            return redirect(request.url)
        
    return render_template('upload.html')


@bp.route('/page2')
@login_required
def page2():
    return 'Page 2'


@bp.route('/submit', methods=['POST'])
@login_required
def submit():
    year_chosen = request.form.get("year_dropdown")
    month_chosen = request.form.get("month_dropdown")
    return 'GÁCHI'