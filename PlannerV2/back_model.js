class Graph{
    constructor(length){
        this.adjlist = [];
        this.length = length;
    }
    hash(key, length){
        index = 0;
        for(let i=0; i<key.length(); i++){
            index += key.charCodeAt(i);
        }
        return index%length;
    }
    add_node(name, price, calories, food_group){
        index = hash(name, length);
        adjlist[index] = FoodNode(price, calories,food_group);
    }
}
class FoodNode{
    constructor(price, calories, food_group){
        this.price = price;
        this.calories = calories;
        this.food_group = food_group;
        this.edges = [];
    }
    update_edges(edge){
        this.edges.append(edge);
    }
}
class Edge{
    constructor(source, destination, discount_value){
        this.source = source;
        this.destination = destination;
        this.discount = discount;
    }   
}