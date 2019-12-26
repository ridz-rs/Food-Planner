import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class plannerController implements EventHandler<ActionEvent>{
	Slider budget;
	Slider calorie;
	Stage stage;
	Scene secondary;
	public plannerController(Slider budget, Slider calorie, Stage stage, Scene secondary) {
		this.budget = budget;
		this.calorie = calorie;
		this.stage = stage;
		this.secondary = secondary;
	}
	@Override
	public void handle(ActionEvent event) {
		Button b1 = (Button)event.getSource();
		try {
			int budget = (int)this.budget.getValue();
			int calorie = (int)this.calorie.getValue();
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

