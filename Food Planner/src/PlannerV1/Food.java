package PlannerV1;

public class Food {
String name;
double price;
double calories;
public Food(String name, double price, double calories) {
	this.name = name;
	this.price = price;
	this.calories = calories;
}
public Food (String name) {
	this.name = name;
}
public void set_price(double price) {
	this.price = price;
}
}
