import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class plannerController implements EventHandler<ActionEvent>{
	TextField budget;
	TextField calorie;
	public plannerController(TextField budget, TextField calorie) {
		this.budget = budget;
		this.calorie = calorie;
	}
	@Override
	public void handle(ActionEvent event) {
		Button b1 = (Button)event.getSource();
		if (b1.getText() == "Set Values") {
			System.out.println(budget.getText() + "," + calorie.getText());
		}
		try {
			Double budgetDouble = Double.parseDouble(this.budget.getText());
			Double calorieDouble = Double.parseDouble(this.calorie.getText());
			// n is a valid integer in here...
			if (validAmount(budgetDouble, calorieDouble) && (b1.getText() == "Set Values")) {
				System.out.println("You inserted correct amounts");
				// Make a main display surface
				Stage stage = new Stage();
                BorderPane mainPane = new BorderPane();
                mainPane.setPadding(new Insets(20));
                // MAIN SCENE 
                Scene mainScene = new Scene(mainPane);            
                
			}
			else {
				System.out.println("sorry please enter correct amount again");
			}
			// this.result.setText(" ");
		} 
		catch(NumberFormatException nfe){
			System.out.println("invalid numbers");
		}
	}
	public boolean validAmount(Double x, Double y) {
		if ((0 <= x) && (x <= 200) && (y <= 2000) && (0 <= y)) {
			return true;
		}
		return false;
	}
}

