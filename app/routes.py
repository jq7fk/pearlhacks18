from app import app
from flask import render_template, request, redirect
from app.forms import LatLong

# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'Jennifer'}
#     posts = [
#         {'author': {'username': 'Bob'}, 'body': 'Hi'},
#         {'author': {'username': 'Alice'}, 'body': 'Sup'}
#     ]
#     return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/user')
def user_pref():
    form = LatLong()
    if form.validate_on_submit():
        return redirect('/result')
    return render_template('user_input.html', title='User Preferences', form=form)

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result_lat = request.form['lat']
        result_long = request.form['long']
        return render_template('result.html', title='Result', result_lat=result_lat, result_long=result_long)