# CarDekho_Used_Car_Price_Prediction
## TECHNOLOGIES
1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Visualization and Machine Learning
## DOMAIN
* Automotive Industry 
* Data Science
* Machine Learning

## PROBLEM STATEMENT:
Imagine you are working as a data scientist in Car Dheko, your aim is to enhance the customer experience and streamline the pricing process by leveraging machine learning. You need to create an accurate and user-friendly streamlit tool that predicts the prices of used cars based on various features. This tool should be deployed as an interactive web application for both customers and sales representatives to use seamlessly.


Data Collected From: https://www.cardekho.com/usedCars

Dataset Link: https://drive.google.com/drive/folders/16U7OH7URsCW0rf91cwyDqEgd9UoeZAJh

Feature Description Link: https://docs.google.com/document/d/1hxW7IvCX5806H0IsG2Zg9WnVIpr2ZPueB4AElMTokGs/edit


## APPROACH:
## 1. Data Processing
* Import and concatenate:
Import all city’s dataset which is in unstructured format.
Convert it into a  structured format.
Add a new column named ‘City’ and assign values for all rows with the name of the respective city.
Concatenate all datasets and make it as a single dataset.
* Handling Missing Values:
Identify and fill or remove missing values in the dataset.
For numerical columns, use techniques like mean, median, or mode imputation.
For categorical columns, use mode imputation or create a new category for missing values.
* Standardising Data Formats:
Check for all data types and do the necessary steps to keep the data in the correct format.
Eg. If a data point has string formats like 70 kms, then remove the unit ‘kms’ and change the data type from string to integers.
* Encoding Categorical Variables:
Convert categorical features into numerical values using encoding techniques.
Use one-hot encoding for nominal categorical variables.
Use label encoding or ordinal encoding for ordinal categorical variables.
* Normalizing Numerical Features:
Scale numerical features to a standard range, usually between 0 and 1.( For necessary algorithms)
Apply techniques like Min-Max Scaling or Standard Scaling.
* Removing Outliers:
Identify and remove or cap outliers in the dataset to avoid skewing the model.
Use IQR (Interquartile Range) method or Z-score analysis.

## 2. Exploratory Data Analysis (EDA)
* Descriptive Statistics:
  Calculate summary statistics to understand the distribution of data.
Mean, median, mode, standard deviation, etc.
* Data Visualization:
  Create visualizations to identify patterns and correlations.
Use scatter plots, histograms, box plots, and correlation heatmaps.
* Feature Selection:
  Identify important features that significantly impact the car prices.
Use techniques like correlation analysis, feature importance from models, and domain knowledge.

## 3. Model Development
* Train-Test Split:
  Split the dataset into training and testing sets to evaluate model performance.Common split ratios are 70-30 or 80-20.
* Model Selection:
  Choose appropriate machine learning algorithms for price prediction.Linear Regression, Decision Trees, Random Forests, Gradient Boosting Machines, etc.
* Model Training:
  Train the selected models on the training dataset. Use cross-validation techniques to ensure robust performance.
* Hyperparameter Tuning:
  Optimize model parameters to improve performance.Use techniques like Grid Search or Random Search.

## 4. Model Evaluation
* Performance Metrics: Evaluate model performance using relevant metrics.
* Mean Absolute Error (MAE), Mean Squared Error (MSE), R-squared.
* Model Comparison: Compare different models based on evaluation metrics to select the best performing model.

## 5. Optimization
* Feature Engineering: Create new features or modify existing ones to improve model performance.
* Use domain knowledge and exploratory data analysis insights.
* Regularization: Apply regularization techniques to prevent overfitting.
* Lasso (L1) and Ridge (L2) regularization.

## 6. Deployment
* Streamlit Application: Deploy the final model using Streamlit to create an interactive web application.
* Allow users to input car features and get real-time price predictions.
* User Interface Design: Ensure the application is user-friendly and intuitive.
* Provide clear instructions and error handling.

## RESULT:
1. A functional and accurate machine learning model for predicting used car prices.
2. Comprehensive analysis and visualizations of the dataset.
3. Detailed documentation explaining the methodology, models, and results.
4. An interactive Streamlit application for real-time price predictions based on user input.


  
