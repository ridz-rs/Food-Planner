package PlannerV1;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.*;
public class PlannerModel extends Observable{
	private Pattern pRestaurantStart = Pattern.compile("(\\w*),*");
	private Pattern pNoSizeStart = Pattern.compile("Name,Calories,Price");
	private Pattern pNoSizeData = Pattern.compile("(\\w+\\s*\\w*),(\\d\\d?\\d?\\d?),\\$?(\\d\\.?\\d?\\d?)");
	private Pattern pNoSizeCombos = Pattern.compile("(.*,),(\\$\\d\\.?\\d?\\d?)");
	private Pattern pRestaurantEnd = Pattern.compile(",*");
	HashMap <String, ArrayList<Food>> planned_meals = new HashMap<String, ArrayList<Food>>();
	static HashMap <String, ArrayList<Food>> data = new HashMap<String, ArrayList<Food>>();
	double price_limit=1000.0;
	double calorie_limit=1000.0;
	public boolean get_data(String filename) { //To be changed
		FileReader f = null;
		try {
		 f = new FileReader(filename);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		BufferedReader bf = new BufferedReader(f);
		String l;
		int state = 0;
		//String curr_rest = null;
		ArrayList<Food> food = new ArrayList<Food>();
		try {
			while ((l= bf.readLine())!=null) {
				switch(state) {
				case 0:
					Matcher m = pRestaurantStart.matcher(l);
					if (m.matches()) {
						state=1;
						food = new ArrayList<Food>();
						data.put(m.group(1), food);
						//curr_rest = m.group(0);
					}
					else { 
						System.out.print("Not Reading Title");
						state =99;
					}
					break;
				case 1:
					if (pNoSizeStart.matcher(l).matches()) state=2;
					else {
						System.out.println("Start format wrong");
						state=99;
					}
					break;
				case 2:
					m = pNoSizeData.matcher(l);
					if (m.matches()) {
						String name = m.group(1);
						double calories = Double.valueOf(m.group(2));
						double price = Double.valueOf(m.group(3));
						food.add(new Food(name,price, calories));
						state = 2; 
					}
					else {
						if (pRestaurantEnd.matcher(l).matches()) state =0;
						else {
							state=99;
							System.out.println("DataFormat wrong"+l);
						}
					}
					break;
				case 99:
					break;
				}
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (state!=99) return true;
		else return false;
	}
	public void get_plan() {
		for (String key: data.keySet()) {
			for (Food food: data.get(key)) {
				if (in_range(food.calories, calorie_limit) && in_range(food.price, price_limit)) {
					if (planned_meals.containsKey(key)) planned_meals.get(key).add(food);
					else {
						ArrayList<Food>lst = new ArrayList<Food>();
						lst.add(food);
						planned_meals.put(key,lst);
					}
				}
			}
		}
		this.notify_all();
	}
	private static boolean in_range(double value, double limit) {
		if ((value>limit-10)&&(value<limit+10)) return true;
		else return false;
	}

	public static void main(String args[]) {
		String filename = "C:\\Projects\\Food-Planner\\Food Planner\\src\\PlannerV1\\PizzaPizzaData.csv";
		PlannerModel model = new PlannerModel();
		System.out.println(model.get_data(filename));
		System.out.println(data.toString());
		model.get_plan();
		System.out.println(model.planned_meals.toString());
		PizzaPizza.menu = data.get("PizzaPizza");
	}
}
