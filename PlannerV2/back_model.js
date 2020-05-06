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