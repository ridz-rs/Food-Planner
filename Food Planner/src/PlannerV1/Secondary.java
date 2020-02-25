package PlannerV1;
import java.util.ArrayList;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class Secondary extends VBox {
	
	public Secondary(int budget, int calorie) {
		 // Start Screen Box
        this.setAlignment(Pos.CENTER);
        this.setPrefSize(600, 450);
        this.setSpacing(20);
        Label welcome = new Label("hAHA"); 
        Font startScreenFont = new Font("Serif",26);    // Making a new Font Object for startBox
        welcome.setFont(startScreenFont);
        
        // Model Collects everything for display
//        PlannerModel planner = new PlannerModel();
		String filename = "C:\\Projects\\Food-Planner\\Food Planner\\src\\PlannerV1\\PizzaPizzaData.csv";
		PlannerModel model = new PlannerModel();
		model.price_limit = budget;
		model.calorie_limit = calorie;
		model.get_data(filename);
		model.get_plan();
		ArrayList<Food>lst = model.planned_meals.get("PizzaPizza");
		for (int i = 0; i < lst.size(); i++) {
			Label lbl = new Label("Name:" + lst.get(i).name + " Price:" + lst.get(i).price + " Calories:" + lst.get(i).calories);
	        lbl.setFont(startScreenFont);
			this.getChildren().add(lbl);
		}
		
		
//		lbl.setText(PlannerModel.data.toString());
		System.out.println(PlannerModel.data.toString());
		System.out.println(PlannerModel.data.get("PizzaPizza").get(0).name);
	}
}
