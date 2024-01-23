from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('salary_predictionLM.joblib')

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    sex = float(request.form.get('sex'))
    age = float(request.form.get('age'))
    designation = float(request.form.get('designation'))
    past_experience = float(request.form.get('past_experience'))

    # Make a prediction using the loaded model
    input_data = [[sex, designation, age, past_experience]]
    prediction = model.predict(input_data)[0]

    # Round the prediction to the nearest integer
    rounded_prediction = round(prediction)

    # Pass the prediction to the HTML template
    return render_template('index.html', prediction=rounded_prediction)

if __name__ == '__main__':
    app.run(debug=True)
