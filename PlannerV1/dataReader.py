import csv
from model import Graph, Vertex

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