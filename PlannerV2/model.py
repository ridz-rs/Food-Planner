import csv
import random
from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/food", methods=['POST'])
def food():
    calorie = float(request.form.get("calorie"))
    price = float(request.form.get("price"))
    graph = initialize_data()
    tup = ()
    out = []
    for i in range(5):
        tup = graph.get_plan(price)
        out.append(tup)
    return render_template("food.html", out=out)


class Vertex:
    def __init__(self, name, calories=None, price=None, food_type=None):
        self.name = name
        self.calories = float(calories)
        self.price = float(price[1:])
        self.neighbours = []
        self.type = food_type.strip()


class Edge:
    def __init__(self, source, destination, discount=0.0, id=None):
        self.source = source
        self.destination = destination
        self.discount = float(discount)
        self.id = id

class Graph:
    def __init__(self, num_vertices):
        self.adj_list = [None for i in range(num_vertices)]
        self.num_vertices = num_vertices

    def hash(self, label):  # returns index of label in the v_list
        i = 0
        for char in label:
            i += ord(char)
        return i % self.num_vertices

    def get(self, label):  # returns the vertex in the graph with the input label
        index = self.hash(label)
        while self.adj_list[index].name != label:
            index += 1
            if index == self.num_vertices:
                index = 0
        return self.adj_list[index]

    def add_vertex(self, node):  # adds a new vertex to the graph
        """
        :param node: Class Vertex
        :return: None
        """
        index = self.hash(node.name)
        while self.adj_list[index] is not None:
            index += 1
            if index == self.num_vertices:
                index = 0
        self.adj_list[index] = node # adding a new node to the graph

    def add_edge(self, v1, v2, discount):
        """
        Adds a weighted edge between two vertices of the graph
        Pre-Condition: source and destination are existing vertices in the graph

        :param v1: Vertex start name
        :param v2: Vertex end name
        :param discount: +ve discount amount between two vertices
        :return: None
        """
        src = self.get(v1)
        dest = self.get(v2)
        src.neighbours.append(Edge(src, dest, float(discount)))

    def display(self):
        for v in self.adj_list:
            print(v.name, "--> ", [neighbour.destination.name for neighbour in v.neighbours])

    def get_min_neighbour(self, vertex, by_calorie=False):
        """

        Extracts the neighbour with the lowest price or calories
        :param vertex: type: class Vertex
        :param by_calorie: refers to whether min is found by calories or price
        :return: type: Edge

        """
        if by_calorie:
            targets = [v.destination.calories for v in vertex.neighbours]
        else:
            targets = [v.destination.price-v.discount for v in vertex.neighbours]
        m = targets[0]
        indices = []  # to store indices of the minimum
        for i in range(len(targets)):
            if targets[i] < m:
                m = targets[i]
                indices = [i]
            elif targets[i] == m:
                indices.append(i)
        min_neighbours = [vertex.neighbours[i] for i in indices]
        return min_neighbours[random.randint(0, len(min_neighbours)-1)]

    def find_type_neighbour(self, typ, quantity):
        quantity_covered = 0
        ret = []
        for v in self.adj_list:
            if quantity_covered == (int)(quantity):
                return ret
            elif v.type == typ.strip():
                ret.append(v)
                quantity_covered += 1
        return ret

    def get_plan(self, target_price):
        plan = []
        prices = []
        total_price = 0
        start = random.randint(0, self.num_vertices-1)
        while self.adj_list[start] in plan:
            start = random.randint(0, self.num_vertices - 1)
        curr = self.adj_list[start]  # start vertex
        curr_price = curr.price
        prices.append(curr_price)
        total_price += curr_price
        while total_price < target_price:
            plan.append(curr)
            total_price += curr_price
            temp_edge = self.get_min_neighbour(curr)
            curr = temp_edge.destination
            curr_price = curr.price - temp_edge.discount
            if total_price > target_price:
                break
            prices.append(curr_price)

        return plan, prices

    def construct_combo(self, dict):
        """
        constructs a combo by placing edge values between vertices of the graph
        :param dict: a dictionary {name:{discount: {type:value}}}
        :return: None
        :precondition: dict has only one name and discount
        """
        name = list(dict.keys())[0]
        discount = list(dict[name].keys())[0]
        targets = []
        for typ,quantity in dict[name][discount].items():
            if typ is not '-':
                targets.extend(self.find_type_neighbour(typ, quantity))
        for node in self.adj_list:
            for n in self.adj_list:
                if n in targets:
                    node.neighbours.append(Edge(node, n, discount, name))
                else:
                    node.neighbours.append(Edge(node, n))


def show_plan(plan, prices):
    total_price = sum([price for price in prices])
    total_calories = sum([item.calories for item in plan])
    print("===================================================================")
    print(" Item            Price           Calories")
    for i in range(len(plan)):
        print(plan[i].name, "            ", prices[i], "          ", plan[i].calories)
    print("Total price: ", total_price)
    print("Total calories: ", total_calories)
    print("===================================================================")


def initialize_data():
    with open("PizzaPizzaData.csv") as db_file:
        db = csv.reader(db_file)
        dict_norm = {}
        dict_comb = {}
        count = 0
        num_vex = 0
        combo = False
        for row in db:
            if count != 2:
                count += 1
                continue
            if row[0] == "Combos":
                combo = True
                continue
            if row[0] == "Quantity1":
                continue
            if combo:
                dict_comb.setdefault(row[7], {row[3]: {row[4]: row[0], row[5]: row[1]}})
            else:
                dict_norm.setdefault(row[0], [row[1], row[2], row[3]])
    # print(dict_norm)
    graph = Graph(len(dict_norm.keys()))
    for key, value in dict_norm.items():
        ver = Vertex(key, value[0], value[1], value[2])
        graph.add_vertex(ver)
    graph.construct_combo(dict_comb)
    return graph
    # graph.display()

