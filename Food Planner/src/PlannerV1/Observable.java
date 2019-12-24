package PlannerV1;
import java.util.ArrayList;

public class Observable {
	ArrayList<Observer> observers = new ArrayList<Observer>();
	public void add(Observer o){
		observers.add(o);
	}
	public void remove(Observer o) {
		observers.remove(o);
	}
	public void notify_all() {
		for (Observer o : observers) {
			o.update(this);
		}
	}
}
