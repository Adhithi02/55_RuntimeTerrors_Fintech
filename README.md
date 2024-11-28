-----------------------------------Problem Definition:-----------------------------

Personal Finance Manager with Smart Saving Planner
Managing personal finances can be time-consuming and complex without the right tools to track expenses, monitor loans, and set savings goals. A streamlined solution is needed to provide actionable insights and personalized saving strategies.

-----------------------------------Key Challenges:---------------------------------

Expense Tracking: Difficulty in recording and categorizing daily expenses.
Borrowing/Lending Management: No organized system to track borrowed or lent money.
Saving Goals: Inability to create a personalized saving plan aligned with income and goals.
Time Constraints: Limited time for manual financial analysis.

-----------------------------------Desired Outcomes:-------------------------------

Clear visualization of spending patterns via dynamic charts.
AI-driven personalized saving plans based on user data.
An intuitive interface for seamless financial management.

-----------------------------------Proposed Solution:------------------------------ 

Expense Management:
Input expenses by item name, cost, and category.
Visualize expenses and borrowed/lent money using dynamic charts.

AI-Powered Smart Saving Planner:
Integrate a  AI tool to review your current budget and suggest adjustments according to your inputs .
Provide tailored recommendations for balancing essential spending, non-essentials, and savings based on your financial situation.

Data Storage and Analysis:
Store and retrieve financial data using local storage or a database.
AI uses stored data to identify spending trends and suggest improvements

------------------------------Actual Working--------------------------------------
1. Expense Management:
   
Input Collection:
Users enter details like Income, Rent, Grocery, Travel, and Other expenses through a web interface built with Flask.

Data Storage & Visualization:
User inputs are dynamically stored and used to generate visualizations of spending patterns (optional feature using a chart library like Chart.js).

3. AI-Powered Smart Saving Planner:
4. 
Data Processing:
The system uses a CSV dataset (realdata.csv) containing historical financial data to train the model.
Pandas library preprocesses the data by ensuring clean column names and structuring it for analysis.

Machine Learning Model:
A RandomForestRegressor (from Scikit-Learn) is trained to predict Savings based on inputs like Income, Rent, Grocery, Travel, and Others.
The trained model identifies patterns and suggests how much a user can potentially save based on their input.

Prediction:
Once the user submits data, the AI model calculates and returns a savings prediction.
The result is displayed on the web page, offering users actionable insights on how much they can save.

3. Expense Adjustment Feature:
   
Dynamic Expense Optimization:
The system can suggest expense adjustments to balance savings and unexpected costs, focusing on reducing non-essential spending like travel or miscellaneous expenses while keeping necessary ones like rent fixed.

Summary of the Workflow:
Input Phase: Users provide data on their income and expenses.

Processing Phase:
Preprocessed by Pandas and passed into the trained RandomForest model.

Output Phase:
Predicts savings and recommends personalized adjustments for better financial management.



Key Technologies Used
Flask: Web application framework for user interaction.
Scikit-Learn: Machine learning library for model training.
Pandas: Data manipulation and cleaning.
RandomForestRegressor: AI model for predicting savings.
Jinja2: Templating engine for dynamic content rendering.

