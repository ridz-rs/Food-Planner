handleFiles();
class Vertex{
    constructor(name, calories=null, price=null, food_type=null){
        this.name = name;
        this.calories = float(calories);
        this.price = float(price.slice(1)); //gets rid of the $
        this.neighbours = [];
        this.type = food_type.trim();

    }
}
class Edge{
    constructor(source, destination, discount=0.0, id = null){
        this.source = source;
        this.destination = destination;
        this.discount = discount;
        this.id = id;
    }
}

class Graph{

    constructor(num_vertices){
        this.adj_list = [];
        for(let i=0;i<num_vertices;i++){
            this.adj_list.push(null);
        }
        this.num_vertices = num_vertices;
    }

    hash(label){
        let index =0;
        for(let i=0;i<length(label);i++){
            index += label.charCodeAt(i);
        }
        return i % this.num_vertices
    }

    get(label){
        let index = this.hash(label);
        while(this.adj_list[index].name != label){
            index+=1;
            if(index==this.num_vertices){
                index = 0;
            }
        }
        return this.adj_list[index];
    }

    add_vertex(node){
        let index = this.hash(node.name);
        while(this.adj_list[index] != null){
            index += 1;
            if(index == this.num_vertices){
                index = 0;
            }
        }
        this.adj_list[index] = node; // adding a new node to the graph
    }

    get_min_neighbour(vertex, by_calorie=false){
        targets = [];
        for(let i= 0; i<length(vertex.neighbours);i++){
            if(by_calorie){
                targets.push(vertex.neighbours[i].destination.calories);
            }
            else{
                targets.push(vertex.neighbours[i].destination.price - vertex.neighbours[i].discount);
            }
        }
        let m = targets[0];
        indices = {};
        for(let i = 0; i<length(targets); i++){
            if(targets[i]<m){
                m = targets[i];
                indices = [i];
            }
            else if (targets[i]==m){
                indeces.append(i);
            }
        }
        min_neighbours = [];
        for(let i=0;i<length(indices);i++){
            min_neighbours.push(vertex.neighbours[indices[i]]);
        }
        return min_neighbours[(int)(Math.random()*length(min_neighbours))];
    }

    find_type_neighbour(typ, quantity){
        var quantity_covered = 0;
        var ret = [];
        for(let v of this.adj_list){
            if(quantity_covered == (int)(quantity))
                return ret;
            else if (v.type == typ.trim()){
                ret.push(v);
                quantity_covered += 1;
            }
        }
        return ret;
    }
    
    get_plan(target_price){
        var plan = [];
        var prices = [];
        total_price = 0;
        start = (int)(Math.random()*this.num_vertices);
        while(plan.includes(this.adj_list[start])){
            start = Math.random()*this.num_vertices;
        }
        var curr = this.adj_list[start];
        var curr_price = curr.price;
        prices.push(curr_price);
        total_price += curr_price;
        while(total_price < target_price){
            plan.push(curr);
            total_price += curr_price;
            let temp_edge = self.get_min_neighbour(curr);
            curr = temp_edge.destination;
            curr_price = curr.price - temp_edge.discount
            if(total_price > target_price){
                break
            }
            prices.push(curr_price);
        }
        return plan, prices;
    }
    construct_combo(dict){
        var name = list(dict.keys())[0];
        var discount = list(dict[name].keys())[0];
        var targets = [];
        for(let i=0; i<length(dict[keys]); i++){
            let typ = dict[keys][i];
            let quantity = dict[typ];
        // for(typ,quantity of dict[name][discount].items()){
            if(typ != "-"){
                targets.push(this.find_type_neighbour(typ, quantity));
            }
        }
        for(let node of this.adj_list){
            for(let n of this.adj_list){
                if(targets.includes(n))
                    node.neighbours.push(Edge(node, n , discount, name));
                else
                    node.neighbours.push(Edge(node, n));
            }
        }
    }
}
function show_plan(plan, prices){
    var total_price = 0;
    var total_calories = 0;
    for(let i=0;i<length(plan);i++){
        total_calories += plan[i].calories;
        total_price += prices[i];
    }
    console.table(plan, ["name", "calories"]);
    console.table(prices);
    console.log(total_calories);
    console.log(total_price);
}

function handleFiles(){
    if(window.FileReader){
    var reader = new FileReader();
    reader.readAsText("PizzaPizzaData.csv");
    reader.onload = loadHandler;
    reader.onerror = errorHandler;
    }
    else{
        alert("File reading not supported by browser");
    }

}
function loadHandler(event){
    var csv = event.target.reasult;
    processData(csv);
}
function processData(csv){
    var allTextLine = csv.split(/\r\n|\n/);
    var lines = [];
    for(var i=0; i<allTextLines.length; i++){
        var data = allTextLines[i].split(';');
        var tarr = [];
        for(var j=0;j<data.length;j++){
            tarr.push(data[j]);
        }
        lines.push(tarr);
    }
    console.log(lines);
}
function errorHandler(evt){
    if(evt.target.error.name=="NotRadableError"){
        alert("Cannot read file!");
    }
}