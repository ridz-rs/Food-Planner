import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class PlannerView extends Application implements Observer{

	@Override
	public void update(Observable o) {
		// TODO Auto-generated method stub
	}
	public static void main(String[] args) {
		launch(args);
	}
	
	public void start(Stage stage) throws Exception {
		initUI(stage);
	}
	
	public void initUI(Stage stage) throws Exception {
		
		Label heading = new Label("Welcome to UTM's Food Planner");
		Label budgetLabel = new Label("Enter your Budget");
		Label calorieLabel = new Label("Enter your Calorie Limit");
		
		TextField budget = new TextField();
		TextField calorieLimit = new TextField();

		
		Slider Budget = new Slider();
		// Create the GUI controller to control the Model
		GridPane mainPage = new GridPane();
		mainPage.setPadding(new Insets(10));

		// Create the buttons
		Button b1 = new Button("Confirm");
		b1.setOnAction(new plannerController(budget, calorieLimit));
		
		mainPage.setHgap(10);
		mainPage.setVgap(10);

		// add them to the contentPane
		mainPage.add(heading, 0, 1);
		mainPage.add(budgetLabel, 0, 2);
		mainPage.add(budget, 0, 3);
		mainPage.add(calorieLabel, 0, 4);
		mainPage.add(calorieLimit, 0, 5);
		mainPage.add(b1, 0, 6);

		// Create button press event handlers
//		ButtonInflateActionListener mb1 = new ButtonInflateActionListener(model_b1);
//		ButtonInflateActionListener mb2 = new ButtonInflateActionListener(model_b2);

		// Tell the buttons who they should call when they are pressed.
		// That is, hook up the controller to the Model.
//		b1.addEventHandler(ActionEvent.ACTION, mb1);
//		b2.addEventHandler(ActionEvent.ACTION, mb2);

		// SCENE
		Scene scene = new Scene(mainPage, 200, 225);

		// STAGE
		stage.setTitle("FoodPlanner");
		stage.setScene(scene);
		stage.show();
	}
}
