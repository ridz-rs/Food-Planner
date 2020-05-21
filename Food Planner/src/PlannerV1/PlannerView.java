package PlannerV1;
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
		PlannerModel model = (PlannerModel)o;
		System.out.println(model.planned_meals.toString());
	}
	public static void main(String[] args) {
		launch(args);
	}
	
	public void start(Stage stage) throws Exception {
		initUI(stage);
	}
	
	public void initUI(Stage stage) throws Exception {
		PlannerModel model = new PlannerModel();
		model.add(this);
		Label heading = new Label("Welcome to UTM's Food Planner");
		Label budgetLabel = new Label("Enter your Budget");
		Label calorieLabel = new Label("Enter your Calorie Limit");
		
		Slider budget = new Slider();
		budget.setMax(200);
		budget.setMin(0);
		budget.setShowTickLabels(true);
		budget.setShowTickMarks(true);
		budget.setMajorTickUnit(50);
		budget.setMinorTickCount(5);
		budget.setBlockIncrement(10);
		
		Slider calorie = new Slider();
		calorie.setMax(5000);
		calorie.setMin(0);
		calorie.setShowTickLabels(true);
		calorie.setShowTickMarks(true);
		calorie.setMajorTickUnit(50);
		calorie.setMinorTickCount(5);
		calorie.setBlockIncrement(10);
		
		GridPane mainPage = new GridPane();
		mainPage.setPadding(new Insets(10));	

		Button b1 = new Button("Confirm");
		b1.setOnAction(new PlannerController(budget, calorie, stage));
		
		mainPage.setHgap(10);
		mainPage.setVgap(10);
		mainPage.add(heading, 5, 1);
		mainPage.add(budgetLabel, 5, 2);
		mainPage.add(budget, 5, 3);
		mainPage.add(calorieLabel, 5, 4);
		mainPage.add(calorie, 5, 5);
		mainPage.add(b1, 5, 6);

		Scene scene = new Scene(mainPage, 500, 500);

		stage.setTitle("FoodPlanner");
		stage.setScene(scene);
		stage.show();
	}
}
