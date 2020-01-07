package PlannerV1;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class PlannerController implements EventHandler<ActionEvent>{
	Slider budget;
	Slider calorie;
	Stage stage;
	Scene secondary;
	PlannerModel model;
	public PlannerController(Slider budget, Slider calorie, Stage stage, Scene secondary, PlannerModel model) {
		this.budget = budget;
		this.calorie = calorie;
		this.stage = stage;
		this.secondary = secondary;
		this.model = model;
	}
	@Override
	public void handle(ActionEvent event) {
		Button b1 = (Button)event.getSource();
		try {
			int budget = (int)this.budget.getValue();
			int calorie = (int)this.calorie.getValue();
			model.price_limit = budget;
			model.calorie_limit = calorie;
			model.get_plan();
			if (validAmount(budget, calorie) && (b1.getText() == "Confirm")) {
				System.out.println("You inserted correct amounts");   
			}
			else {
				System.out.println("sorry please enter correct amount again");
			}
			// this.result.setText(" ");
		} 
		catch(NumberFormatException nfe){
			System.out.println("invalid numbers");
		}
		if (b1.getText() == "Confirm") {
			stage.setScene(secondary);
		}
	}
	
	public boolean validAmount(int x, int y) {
		if ((0 <= x) && (x <= 200) && (y <= 2000) && (0 <= y)) {
			return true;
		}
		return false;
	}
}

