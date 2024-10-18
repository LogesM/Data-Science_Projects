# Microsoft : Classifying Cybersecurity Incidents with Machine Learning
## TECHNOLOGIES USED
1. Data Preprocessing and Feature Engineering
2. Machine Learning Classification Techniques
3. Model Evaluation Metrics (Macro-F1 Score, Precision, Recall)
4. Cybersecurity Concepts and Frameworks (MITRE ATTACK)

## DOMAIN
* Cyber Security
* Machine Learning
  
## PROBLEM STATEMENT:
Imagine you are working as a data scientist at Microsoft, tasked with enhancing the efficiency of Security Operation Centers (SOCs) by developing a machine learning model that can accurately predict the triage grade of cybersecurity incidents. Utilizing the comprehensive GUIDE dataset, your goal is to create a classification model that categorizes incidents as true positive (TP), benign positive (BP), or false positive (FP) based on historical evidence and customer responses. The model should be robust enough to support guided response systems in providing SOC analysts with precise, context-rich recommendations, ultimately improving the overall security posture of enterprise environments.
You need to train the model using the train.csv dataset and provide evaluation metrics—macro-F1 score, precision, and recall—based on the model's performance on the test.csv dataset. This ensures that the model is not only well-trained but also generalizes effectively to unseen data, making it reliable for real-world applications.

Dataset Link - https://drive.google.com/drive/folders/18vt2lkf69MggXitrTSn9qnZ8s-ToeKcH

## APPROACH:
## 1. Data Exploration and Understanding:
* Initial Inspection: Start by loading the train.csv dataset and perform an initial inspection to understand the structure of the data, including the number of features, types of variables (categorical, numerical), and the distribution of the target variable (TP, BP, FP).
* Exploratory Data Analysis (EDA): Use visualizations and statistical summaries to identify patterns, correlations, and potential anomalies in the data. Pay special attention to class imbalances, as they may require specific handling strategies later on.
## 2. Data Preprocessing:
* Handling Missing Data: Identify any missing values in the dataset and decide on an appropriate strategy, such as imputation, removing affected rows, or using models that can handle missing data inherently.
* Feature Engineering: Create new features or modify existing ones to improve model performance. For example, combining related features, deriving new features from timestamps (like hour of the day or day of the week), or normalizing numerical variables.
* Encoding Categorical Variables: Convert categorical features into numerical representations using techniques like one-hot encoding, label encoding, or target encoding, depending on the nature of the feature and its relationship with the target variable.
## 3. Data Splitting:
* Train-Validation Split: Before diving into model training, split the train.csv data into training and validation sets. This allows for tuning and evaluating the model before final testing on test.csv. Typically, a 70-30 or 80-20 split is used, but this can vary depending on the dataset's size.
* Stratification: If the target variable is imbalanced, consider using stratified sampling to ensure that both the training and validation sets have similar class distributions.
## 4. Model Selection and Training:
* Baseline Model: Start with a simple baseline model, such as a logistic regression or decision tree, to establish a performance benchmark. This helps in understanding how complex the model needs to be.
* Advanced Models: Experiment with more sophisticated models such as Random Forests, Gradient Boosting Machines (e.g., XGBoost, LightGBM), and Neural Networks. Each model should be tuned using techniques like grid search or random search over hyperparameters.
* Cross-Validation: Implement cross-validation (e.g., k-fold cross-validation) to ensure the model's performance is consistent across different subsets of the data. This reduces the risk of overfitting and provides a more reliable estimate of the model's performance.
## 5. Model Evaluation and Tuning:
* Performance Metrics: Evaluate the model using the validation set, focusing on macro-F1 score, precision, and recall. Analyze these metrics across different classes (TP, BP, FP) to ensure balanced performance.
* Hyperparameter Tuning: Based on the initial evaluation, fine-tune hyperparameters to optimize model performance. This may involve adjusting learning rates, regularization parameters, tree depths, or the number of estimators, depending on the model type.
* Handling Class Imbalance: If class imbalance is a significant issue, consider techniques such as SMOTE (Synthetic Minority Over-sampling Technique), adjusting class weights, or using ensemble methods to boost the model's ability to handle minority classes effectively.
## 6. Model Interpretation:
* Feature Importance: After selecting the best model, analyze feature importance to understand which features contribute most to the predictions. This can be done using methods like SHAP values, permutation importance, or model-specific feature importance measures.
* Error Analysis: Perform an error analysis to identify common misclassifications. This can provide insights into potential improvements, such as additional feature engineering or refining the model's complexity.
## 7. Final Evaluation on Test Set:
* Testing: Once the model is finalized and optimized, evaluate it on the test.csv dataset. Report the final macro-F1 score, precision, and recall to assess how well the model generalizes to unseen data.
* Comparison to Baseline: Compare the performance on the test set to the baseline model and initial validation results to ensure consistency and improvement.

## RESULT: 
By the end of the project, learners should aim to achieve the following outcomes:
* A machine learning model capable of accurately predicting the triage grade of cybersecurity incidents (TP, BP, FP) with high macro-F1 score, precision, and recall.
* A comprehensive analysis of model performance, including insights into which features are most influential in the prediction process.
* Documentation that details the model development process, including data preprocessing, model selection, evaluation, and potential deployment strategies.

