# Life Expectancy Prediction with Decision Tree

This project predicts life expectancy using a Decision Tree Regressor trained on the "Life Expectancy Data.csv" dataset.

## Project Structure

- [app.py](app.py): Flask web application for making predictions.
- [Life Expectancy Data.csv](Life%20Expectancy%20Data.csv): Dataset used for training.
- [life_expectancy_model.pkl](life_expectancy_model.pkl): Trained model file.
- [model.ipynb](model.ipynb): Jupyter notebook for data analysis and model training.
- [requirements.txt](requirements.txt): Python dependencies.
- [static/style.css](static/style.css): Stylesheet for the web app.
- [templates/index.html](templates/index.html): HTML template for the web app.

## How to Run

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Train the model (optional):**
    - Open and run all cells in [model.ipynb](model.ipynb) to retrain and save the model as `life_expectancy_model.pkl`.

3. **Start the web app:**
    ```sh
    python app.py
    ```
    - The app will be available at `http://127.0.0.1:5000/`.

4. **Use the Predictor:**
    - Enter the required features in the form and get the predicted life expectancy.

## Features Used

- Country
- Status (Developed/Developing)
- Year
- Adult Mortality
- Alcohol
- BMI
- Schooling
- GDP
- Population

## Model

- Decision Tree Regressor (`sklearn.tree.DecisionTreeRegressor`)
- Preprocessing: Label encoding for categorical features, missing value removal

## License

This project is for educational purposes.