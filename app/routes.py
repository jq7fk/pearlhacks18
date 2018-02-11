from app import app
from flask import render_template, request, redirect
from app.forms import LatLong, Favorites
import requests
# import graphlab

# import pandas as pa
#
# train model
# restaurants= []
# train_data = restaurants
# item_sim_model = graphlab.item_similarity_recommender.create(train_data, target='rating', similarity_type='pearson')
#
# make recommendations
# item_sim_recom = item_sim_model.recommend(users=range(1,6), k = 5)
# item_sim_recom.print_rows(num_rows=10)

API_KEY = "9FI5hAiEmJXs76PnZeyMydrSa-9eb8-UdG1LloXLifpo7GYjA8kyjg1qOeGzJKGeKmx7QECBdJs3q2IqZhNrTxXk9G_yRfYRton4lxv08bNt8U9sJRs5XRoWYZ1_WnYx"


def request_info(api_key, url_params=None):
    url_params = url_params or {}
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {'Authorization': 'Bearer %s' % api_key,}
    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()['businesses']

@app.route('/user')
def user_pref():
    form = LatLong()
    if form.validate_on_submit():
        return redirect('/result')
    return render_template('user_input.html', title='User Preferences', form=form)

def processJSON():
    form = LatLong()
    restaurants = []
    result_start = form.start.data
    result_price = form.price.data
    url_params = {'price': result_price, 'location': result_start}
    result1 = request_info(API_KEY, url_params)
    for entry in result1:
        restaurants.append(entry['name'])
    return restaurants

def processJSON2():
    restaurants2 = []
    result_end = LatLong().start.data
    result_price = LatLong().price.data
    url_params2 = {'price': '2', 'location': '22903'}
    result2 = request_info(API_KEY, url_params2)
    for entry in result2:
        restaurants2.append(entry['name'])
    return restaurants2

@app.route('/result', methods=['POST', 'GET'])
def result():
    form = Favorites
    if request.method == 'POST':
        result = processJSON()
        return render_template('result.html', title='Result', result=result, form=form)

@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    form = Favorites
    if request.method == 'GET':
        result = processJSON2()
        return render_template('recommend.html', title='Result', result=result, form=form)