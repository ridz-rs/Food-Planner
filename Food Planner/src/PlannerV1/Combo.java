package PlannerV1;
import java.util.*;
public class Combo {
	public String name;
	public ArrayList<Food> food;
	public double price;
	public Combo(String name, ArrayList<Food>food, double price) {
		this.name = name;
		this.food = food;
		this.price = price;
	}
public boolean check_validity(double price, double calories) {
	double total_calories=0.0;
	for (Food f: this.food) {
		total_calories += f.calories;
	}
	if (this.price<price && total_calories<calories) return true;
	else return false;
}
}
