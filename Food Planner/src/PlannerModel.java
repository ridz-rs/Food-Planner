// import java.util.HashMap;
import java.util.*;
import java.util.ArrayList;
public class PlannerModel extends Observable{
HashMap <String, ArrayList<Food>> planned_meals = new HashMap<String, ArrayList<Food>>();
HashMap <String, ArrayList<Food>> sample_data = new HashMap<String, ArrayList<Food>>();
ArrayList<Food> pizza = new ArrayList<Food>();
ArrayList<Food> timhortons = new ArrayList<Food>();
public void sample_data_loader() {
	this.pizza.add(new Food("CheeseSlice", 3.99));
	this.pizza.add(new Food("PepperoniSlice", 3.99));
	this.pizza.add(new Food("HawaiianSlice", 4.59));
	this.pizza.add(new Food("ChickenSlice", 4.59));
	this.pizza.add(new Food("MeatSlice", 4.59));
	this.pizza.add(new Food("VeggieMedleySlice", 4.59));
	this.pizza.add(new Food("SuperPlantSlice", 4.59));
	this.timhortons.add(new Food("HotChocolate", 1.99));
	this.timhortons.add(new Food("CandyCaneHotChocolate", 2.69));
	this.timhortons.add(new Food("CandyCaneWhiteChocolate", 2.69));
	this.timhortons.add(new Food("WhiteChocolate", 1.99));
	this.timhortons.add(new Food("IcedCappOriginal", 2.99));
	this.timhortons.add(new Food("IcedCappMocha", 3.79));
	this.timhortons.add(new Food("IcedCappGingerbread", 3.79));
	this.timhortons.add(new Food("IcedCappVanilla", 3.79));
	this.timhortons.add(new Food("IcedCappCaramel", 3.79));
	this.timhortons.add(new Food("IcedCoffee", 1.99));
	this.timhortons.add(new Food("Decaf", 1.76));
	this.timhortons.add(new Food("OriginalBlend", 1.76));
	this.timhortons.add(new Food("DarkRoast", 1.76));
	this.timhortons.add(new Food("Latte", 3.09));
	this.timhortons.add(new Food("FrenchVanilla", 2.29));
	this.timhortons.add(new Food("Mocha", 1.99));
	this.sample_data.put("timhortons", timhortons);
	this.sample_data.put("Pizzapizza", pizza);
}

}