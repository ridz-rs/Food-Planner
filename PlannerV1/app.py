from flask import Flask, request
from flask.templating import render_template
from flask_scss import Scss
from dataReader import initialize_data
from model import Graph
import ast

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/image_folder'
Scss(app, static_dir='static', asset_dir='static/css')

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/plans", methods=['POST'])
def plans():
    calorie = float(request.form.get("calorie"))
    price = float(request.form.get("price"))
    graph = initialize_data()
    plan_lst = []
    price_lst = []
    calorie_lst = []
    tup = ()
    for i in range(5):
        tup = graph.get_plan(price, calorie)
        plan_lst.append(tup[0])
        price_lst.append(round(sum(tup[1]),2))
        calorie_lst.append(sum([item['calories'] for item in plan_lst[i]]))
    print(calorie_lst)
    return render_template("plans.html", plans=plan_lst, prices=price_lst,\
        total_results = len(plan_lst), total_calories = calorie_lst)

@app.route("/details", methods=['GET', 'POST'])
def details():
    plan = request.args.getlist('plan', None)
    item_lst = [ast.literal_eval(item) for item in plan]
    return render_template("details.html", items = item_lst)

if __name__=="__main__":
    app.run(debug=1)