import csv
from model import Graph, Vertex

def initialize_data():
    num_lines = sum(1 for line in open('data_files/FoodData.csv'))
    graph = Graph(num_lines-1)
    with open("data_files/FoodData.csv") as db_file:
        db_file.readline()
        db = csv.reader(db_file)
        for row in db:
            ver = Vertex(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) # Name, Calories, Price, Type, Size, Genre, Location, img_path
            graph.add_vertex(ver)
    with open("data_files/ComboData.csv", 'r') as db_file:
        db = csv.DictReader(db_file)
        data_lst = list(db)
        graph.connect_graph(data_lst)
        # print(data_lst)
    # graph.display()
    return graph

initialize_data()