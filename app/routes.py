from flask import render_template, request
from app import app
from app.calculations import calculate_window_dimensions, calculate_cost, get_number_of_pieces


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        window_count = int(request.form['window_count'])
        mt_total = 0
        p_total = 0
        window_dimensions = {}
        num_pieces = get_number_of_pieces()

        for i in range(1, window_count + 1):
            x1 = float(request.form[f'x1_{i}'])
            x2 = float(request.form[f'x2_{i}'])
            q = float(request.form[f'q_{i}'])
            mp = float(request.form[f'mp_{i}'])

            window_dimensions[i] = calculate_window_dimensions(x1, x2, q)
            mt = (x1 * x2) / 10000
            mt_total += mt
            p_total += calculate_cost(mt, mp)

        return render_template('result.html', window_dimensions=window_dimensions,
                               mt_total=mt_total, p_total=p_total,
                               num_pieces=num_pieces)

    return render_template('index.html')