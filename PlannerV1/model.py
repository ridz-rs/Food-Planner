import random

class Vertex:
    def __init__(self, name, calories, price=None, food_type=None, size=None ,genre=None, location=None,img_path=None):
        self.name = name
        self.calories = float(calories)
        self.price = float(price.strip('$'))
        self.neighbours = []
        self.type = food_type.strip()
        self.genre = genre
        self.size = size
        self.location=location
        self.img_path = img_path
        self.label = self.name+self.type+self.location

    def json_encoder(self):
        return{
                'name': self.name,
                'calories': self.calories,
                'price': self.price,
                'type':  self.type,
                'img_path': self.img_path,
                'location': self.location
        }


class Edge:
    def __init__(self, source, destination, discount=0.0, location=None ,id=None):
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
        while self.adj_list[index].label != label:
            index += 1
            if index == self.num_vertices:
                index = 0
        return self.adj_list[index]

    def add_vertex(self, node):  # adds a new vertex to the graph
        """
        :param node: Class Vertex
        :return: None
        """
        index = self.hash(node.label)
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

    def get_same(self, vertex, same_by):
        """
            returns a neighbour with the same property as specified by same_by
            possible same_by values: location, genre, building, dietary
            dietary is a list of strings
            
        """
        possible_options = [] # list of possible edges
        if same_by== 'dietary':
            pass
        else:
            for edge in vertex.neighbours:
                if same_by == 'location':
                    if edge.destination.location == vertex.location:
                        possible_options.append(edge)
                elif same_by == 'genre':
                    if edge.destination.genre == vertex.genre:
                        possible_options.append(edge)
                elif same_by == 'building':
                    if edge.destination.building == vertex.building:
                        possible_options.append(edge)
        return possible_options[random.randint(0, len(possible_options)-1)]
            
    def find_type_neighbour(self, typ, quantity):
        """
            typ: String containing the type wanted
            quantity: String containing number of typ wanted
            Returns a list of quantity amount of vertices from the adj_list of the graph
        """
        if typ=='-':
            return []
        quantity_covered = 0
        ret = []
        for v in self.adj_list:
            if quantity_covered == (int)(quantity):
                return ret
            elif v.type == typ.strip():
                ret.append(v)
                quantity_covered += 1
        return ret

    def get_destination(self, curr, find_neighbour_function):
        if find_neighbour_function=="min_neighbour":
            temp_edge = self.get_min_neighbour(curr) # try get_same_restaurant_neighbour, get_beverage_neighbour
        elif find_neighbour_function=="min_neighbour_calories":
            temp_edge = self.get_min_neighbour(curr,True)
        elif find_neighbour_function=="get_same_genre":
            temp_edge = self.get_same(curr,'genre')
        elif find_neighbour_function=="get_same_location":
            temp_edge = self.get_same(curr, 'location')
        elif find_neighbour_function=="get_same_building":
            temp_edge = self.get_same(curr,'building')
        return temp_edge

    def get_plan(self, target_price, target_calories, find_neighbour_function):
        """

        Returns a plan within the price and calorie constraints.  
        find_neighbour_function: min_neighbour, min_neighbour_calories, get_same_genre, get_same_location, get_same_building
        :return: ([json], [float])
        """
        plan = []
        count = dict({})
        prices = []
        total_price = 0
        total_calories = 0
        start = random.randint(0, self.num_vertices-1) # get a random index
        while not (self.adj_list[start].price< target_price and self.adj_list[start].calories<target_calories): 
            start = random.randint(0, self.num_vertices - 1)
        curr = self.adj_list[start]  # start vertex
        curr_price = curr.price 
        while total_price < target_price and total_calories<target_calories:
            plan.append(curr)
            if curr.name in count.keys():
                count[curr.name] += 1
            else:
                count.setdefault(curr.name, 1)
            total_price += curr_price
            total_calories += curr.calories
            temp_edge = self.get_destination(curr, find_neighbour_function)
            curr = temp_edge.destination
            curr_price = curr.price - temp_edge.discount # calculating discount for combo
            if total_price > target_price or total_calories>target_calories:
                plan.pop()
                total_price -= curr_price
                total_calories -= curr.calories
                break
            prices.append(curr_price)
        plan = [v.json_encoder() for v in plan]
        return plan, prices

    def connect_graph(self, lst):
        """
        Connnect the vertices of the graph.
        :param lst: A list of Dictionary with data parameters
        :return: None
        """
        for vertex in self.adj_list:
            for node in self.adj_list:
                if vertex.name == "Fountain" and node.name=="Fountain":
                    continue
                vertex.neighbours.append(Edge(vertex, node))
            
    def create_combos(self):
        pass


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


