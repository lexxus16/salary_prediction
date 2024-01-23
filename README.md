# Salary Prediction

This project was developed during my internship at Mentorness and it focuses on predicting salaries for data professionals. It leverages Flask to deploy a machine-learning model to provide a user-friendly web interface for seamless predictions.


## Introduction

This project navigates through data science methodologies, starting with Exploratory Data Analysis (EDA) for insightful salary patterns. The Feature engineering and preprocessing prepare the data for diverse machine learning models. Employing ML pipelines, the project streamlines processes and deploys a model for predictions. It offers actionable recommendations, enhancing understanding of factors influencing salaries in data professions. Finally, It is deployed using Flask with an interactive interface allowing users to input their details and get their predicted salary.


## Model Training and Selection

In search of the most robust model for the data, five regression algorithms were evaluated: Linear Regression, KNN, Random Forest, Decision Tree, and Gradient Boosting. KNN distinguished itself through its inherent flexibility in capturing non-linear relationships and its robustness to outliers, making it the most effective choice for accurate prediction in this project.


## Model Deployment

The machine learning model is deployed using Flask, enabling a user-friendly web interface for predicting salaries.


## Usage

To run the app, execute the following command in your terminal:

```bash
python app.py
```
Then, visit http://127.0.0.1:5000 in your web browser to access the web interface.


## Screenshot

<p align="center">
  <img src="https://github.com/lexxus16/salary_prediction/assets/69308391/788d77d9-2f05-42f3-884e-02ceea1f7ad4" alt="Alt Text" width="520"/>
</p>


## Dependencies

Ensure you have the following dependencies installed:

- Pandas
- NumPy
- Flask
- Matplotlib
- Seaborn
- Sklearn
- Joblib


## Contributing

You are welcome to contribute to enhancing and improving this project. You can contribute in the following ways:

- **Bug Reports:** If you come across any issues or unexpected behavior, please report them.

- **Feature Requests:** If you have ideas for new features or improvements, feel free to submit a feature request.

- **Code Contributions:** If you are interested in contributing directly to the codebase, fork the repository, make your changes, and submit a pull request.
