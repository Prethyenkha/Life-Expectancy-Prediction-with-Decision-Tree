from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = joblib.load("life_expectancy_model.pkl")
le_country = joblib.load("le_country.pkl")
le_status = joblib.load("le_status.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Get input values
            country = le_country.transform([request.form["Country"]])[0]
            status = le_status.transform([request.form["Status"]])[0]
            year = int(request.form["Year"])
            adult_mortality = float(request.form["AdultMortality"])
            alcohol = float(request.form["Alcohol"])
            bmi = float(request.form["BMI"])
            schooling = float(request.form["Schooling"])
            gdp = float(request.form["GDP"])
            population = float(request.form["Population"])

            # You can add more fields here as needed

            features = np.array([[country, year, status, adult_mortality, alcohol, bmi, schooling, gdp, population]])

            prediction = round(model.predict(features)[0], 2)
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
