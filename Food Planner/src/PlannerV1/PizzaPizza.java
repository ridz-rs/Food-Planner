package PlannerV1;
import java.util.*;
public class PizzaPizza {
	static ArrayList<Food> menu = new ArrayList<Food>();
	static ArrayList<Food> classicslices=new ArrayList<Food>();
	static ArrayList<Food> premiumslices=new ArrayList<Food>();
	static ArrayList<Food> fullpizzas=new ArrayList<Food>();
	static ArrayList<Food> dips=new ArrayList<Food>();
	static ArrayList<Food> fountain=new ArrayList<Food>();
	static ArrayList<Food> chips=new ArrayList<Food>();
	static ArrayList<ArrayList<Food>> Combo1=new ArrayList<ArrayList<Food>>();
	public PizzaPizza() {
		menu = PlannerModel.data.get("PizzaPizza");
		for(Food f:menu) {
			if (f.name.equals("Pepperoni Slice")||f.name.equals("Cheese")) classicslices.add(f);
			else if (f.name.equals("Veggie Medley") || f.name.equals("Meat Lovers")||f.name.equals("Chicken")|| f.name.equals("Hawaiian")||f.name.equals("Super plant")) premiumslices.add(f);
			else if (f.name.equals("18' Classic Pizza")) fullpizzas.add(f);
			else;
		}
	}
	
}
				