## Day 3. 100 Days of Data Science Challenge - 05/06/2024

## Building a Calorie Intake Calculator

### Aim:
Develop a new app feature with your Python skills to calculate calories and nutrition values from user input.

### Project Description:
Join a Health and Leisure company as a Software Engineer to add an exciting new feature to the app.

This project will utilize your Python skills to build a function that calculates calories and nutrition values from user input. Dive in and help customers make informed dietary choices and improve their health!

### Diet Coach App -

#### Nutritional Summary Function:

Enhance the Diet Coach app by creating the ``nutritional_summary()`` function to calculate and return the total nutritional values from the ``nutrition_dict`` dataset.

#### Function Output:

- If all the foods are present in the dataset, the function returns a dictionary with keys: ``"calories"``, ``"total_fat"``, ``"protein"``, ``"carbohydrate"``, and ``"sugars"``.

- If any food is missing from the dataset, the function returns the name of the **first missing item**.

#### Input Format:

- **Dictionary:** For example, calling ``nutritional_summary({"Croissants, cheese": 150, "Orange juice, raw": 250})`` should output ``{'calories': 733.5, 'total_fat': 32.0, 'protein': 15.55, 'carbohydrate': 96.5, 'sugars': 38.025}`` Here, 150 and 250 represent the grams of each food.

- **Handling non-existent keys:** For example, calling ``nutritional_summary({"Croissant": 150, "Orange juice": 250})`` should output ``"Croissant"``.

---

*This project is part of the 100 Days of Data Science Challenge. For daily updates and progress, visit the [GitHub repository](https://github.com/vatsalparikh07/100-days-of-data-science-challenge/tree/main).* 
