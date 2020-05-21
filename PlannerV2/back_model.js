class FoodNode{
    constructor(name, price, calories, food_group){
        this.name = name;
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
class Graph{
    constructor(length){
        this.adj_list = [];
        for(var i =0;i<length;i++){
            this.adj_list.append(null);
        }
        this.length = length;
    }
    hash_fnc(node){
        var index;
        for(var i=0;i<node.name.length;i++){
            index += node.name.charCodeAt(i);
        }
        return index%this.length;
    }
    insert_node(node){
        var index = this.hash_fnc(node);
        while(this.adj_list[index]!=null){
            index++;
        }
        this.adj_list[index] = node;
        for(var i=0; i<this.length; i++){
            
        }
    }
}