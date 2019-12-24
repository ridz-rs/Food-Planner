package PlannerV1;

public class Beverage extends Food{
	String size;
	public Beverage(String name, double price, String size) {
		super(name, price);
		this.size = size;
	}
}
