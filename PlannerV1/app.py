from flask import Flask, request
from flask.templating import render_template
from flask_scss import Scss
from dataReader import initialize_data
from model import Graph
import model
import ast

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/image_folder'
# Scss(app, static_dir='static', asset_dir='static/css')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        building = request.form["building"]
        print(building)
        same_restaurant = request.form["same_restaurant"]
        print(same_restaurant)
        genre = request.form["genre"]
        print(genre)
        max_quant = request.form["max_quant"]
        print(max_quant)
        return render_template("index.html", building=building, same_restaurant=same_restaurant, genre=genre,max_quant=max_quant)
    else:
        return render_template("index.html")


@app.route("/plans", methods=['POST'])
def plans():
    calorie = float(request.form.get("calorie"))
    price = float(request.form.get("price"))
    graph = initialize_data()
    plan_lst = []
    price_lst = []
    calorie_lst = []
    num_location_lst = []
    tup = ()
    option_list = ['min_neighbour','min_neighbour_calories', 'get_same_location', 'get_same_genre']
    for i in range(4): # gets 4 plans 
        tup = graph.get_plan(price, calorie, option_list[i])
        if len(tup[0])==0:
            continue
        plan_lst.append(tup[0])
        num_location_lst.append(get_num_location(tup[0]))
        price_lst.append(round(sum(tup[1]),2))
        calorie_lst.append(sum([item['calories'] for item in tup[0]]))
    return render_template("plans.html", plans=plan_lst, prices=price_lst,\
        total_results = len(plan_lst), total_calories = calorie_lst, \
            num_location_lst=num_location_lst)

@app.route("/details", methods=['GET', 'POST'])
def details():
    plan = request.args.getlist('plan', None)
    item_lst = [ast.literal_eval(item) for item in plan]
    return render_template("details.html", items = item_lst)


def get_num_location(lst):
    """
        Returns number of locations in the plan described by plan_lst
    """
    count = 0
    locations = []
    for item in lst:
        if item['location'] not in locations:
            locations.append(item['location'])
            count += 1
    return count

def apply_filters():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=1, host="10.10.10.1")