from flask import Flask, request, render_template
import warnings
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

warnings.filterwarnings("ignore", category=UserWarning, module='sklearn')

# Load the dataset
data = pd.read_csv('realdata.csv')
data.columns = data.columns.str.strip()

X = data[['Income', 'Rent', 'Grocery', 'Travelling', 'Others']]
y = data['Savings']

# Train the Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, 'savings_model.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    income = float(request.form['income'])
    rent = float(request.form['rent'])
    grocery = float(request.form['grocery'])
    travel = float(request.form['travel'])
    others = float(request.form['others'])
    additional_expense = float(request.form['additional_expense'])

    model = joblib.load('savings_model.pkl')
    user_input = [[income, rent, grocery, travel, others]]
    predicted_savings = model.predict(user_input)

    # Existing adjust_expenses function
    def adjust_expenses(income, rent, grocery, travel, others, additional_expense):
        max_grocery_reduction = 0.10
        max_travel_reduction = 0.20
        max_other_reduction = 0.30
        required_adjustment = additional_expense

        grocery_adjustment = grocery * max_grocery_reduction
        travel_adjustment = travel * max_travel_reduction
        other_adjustment = (income - rent - grocery - travel) * max_other_reduction

        adjusted_grocery = grocery - min(grocery_adjustment, required_adjustment)
        required_adjustment -= min(grocery_adjustment, required_adjustment)

        adjusted_travel = travel - min(travel_adjustment, required_adjustment)
        required_adjustment -= min(travel_adjustment, required_adjustment)

        adjusted_others = (income - rent - grocery - travel) - min(other_adjustment, required_adjustment)
        required_adjustment -= min(other_adjustment, required_adjustment)

        if required_adjustment > 0:
            return "Expense is not valid! You cannot afford this expense."

        savings = income - rent - adjusted_grocery - adjusted_travel - adjusted_others
        if savings < 0:
            return "Savings cannot be negative! You need to reduce your expenses further."

        return f"Expense is valid! Adjust your expenses as follows: {{'grocery': {adjusted_grocery}, 'travel': {adjusted_travel}, 'others': {adjusted_others}}}\nUpdated Savings: {savings}"

    result = adjust_expenses(income, rent, grocery, travel, others, additional_expense)
    return render_template('result.html', savings=predicted_savings[0], result=result)

if __name__ == '__main__':
    app.run(debug=True)
