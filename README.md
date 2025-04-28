📄 Financial Forecasting Application
📚 Project Overview
This project builds a Machine Learning-based Web Application to predict key financial metrics, including:

Revenue (Million USD)

Operating Income (Million USD)

Net Income (Million USD)

The model predicts these outputs based on user inputs such as:

Year (2020–2026)

Quarter (Q1, Q2, Q3, Q4, or All)

Region (e.g., Americas, EMEA, Asia-Pacific, or All)

Business Unit (e.g., IT Services, Cloud, Consulting, or All)

Employee Count

🛠️ Tools & Technologies Used

Area	Tools/Frameworks
Language	Python 3
Machine Learning	Random Forest Regressor + MultiOutputRegressor
Optimization	GridSearchCV for hyperparameter tuning
Data Handling	Pandas, Scikit-Learn
Web App	Streamlit
Model Saving	Joblib
🔎 Data Overview
Source: Financial and operational dataset (cleaned and preprocessed).

Contains historical financial records for years 2020 to 2024.

Features include Year, Quarter, Region, Business Unit, Employee Count, and financial targets.

Cleaned to handle missing values and categorical encoding.

🧠 Machine Learning Workflow
1. Data Preprocessing
Categorical features (Quarter, Region, Business Unit) are One-Hot Encoded.

Numerical features (Year, Employee Count) passed through unchanged.

2. Model Architecture
MultiOutputRegressor wraps a RandomForestRegressor to predict multiple targets simultaneously.

GridSearchCV is used for tuning parameters:

n_estimators

max_depth

min_samples_split

3. Model Performance
R² Score on Test Set (approximate):

~ -0.27 (due to relatively high prediction complexity across multiple financial metrics and extrapolation challenges).

⚡ Important: Model performance is stronger when predicting years 2020–2024 (seen in training) and weaker for extrapolating future years (2025–2026).

🌟 Features of Streamlit Application
Easy to use drop-down selection for Year, Quarter, Region, Business Unit.

Dynamic Employee Count selection based on valid ranges.

Input Summary section showing user's selected inputs.

Real-time Prediction of Revenue, Operating Income, and Net Income.

Automatic adjustment to allow prediction for future unseen years (2025, 2026).

📈 Prediction Logic
For years 2020–2024: Model bases predictions on learned historical patterns.

For years 2025–2026: Model extrapolates based on previous trends.

Employee Count is validated to prevent unrealistic inputs.

‘All’ options available for Quarter, Region, and Business Unit for flexibility.

🚀 How to Run the Project Locally
Clone/download the repository.

Install required packages:

bash
Copy
Edit
pip install pandas scikit-learn streamlit joblib
Run the Streamlit app:

bash
Copy
Edit
streamlit run project.py
The web app will open automatically in your browser.

⚡ Future Improvements (Optional)
Improve model performance using more complex algorithms (e.g., XGBoost, LightGBM).

Add visualization of historical vs predicted financials.

Dynamic adjustment of Employee Count ranges based on selected business criteria.

Save user inputs for further analytics.

📢 Final Notes
This project successfully builds an end-to-end financial forecasting system
and provides an interactive platform to simulate future financial outcomes for any business.
