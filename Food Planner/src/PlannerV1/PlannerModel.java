package PlannerV1;
import java.util.*;
import java.io.*;
public class PlannerModel extends Observable{
HashMap <String, ArrayList<Food>> planned_meals = new HashMap<String, ArrayList<Food>>();
static HashMap <String, ArrayList<Food>> data = new HashMap<String, ArrayList<Food>>();
public static void get_data(String filename) { //To be changed
	PizzaPizza pizzapizza = new PizzaPizza();
	pizzapizza.add(new Food("Pepperoni Slice", 3.99));
	pizzapizza.add(new Food("Cheese Slice", 3.99));
	pizzapizza.add(new Food("Chicken Slice", 4.59));
	pizzapizza.add(new Food("Meat Lovers Slice", 4.59));
	pizzapizza.add(new Food("Veggie Medley Slice", 4.59));
	pizzapizza.add(new Food("Super Plant Slice", 3.99));
	pizzapizza.add(new Food("Pepperoni Slice", 3.99));
}
}
