# Import necessary libraries
from flask import Flask, render_template, request
import joblib

# Load the trained KNN classifier
knn_model = joblib.load('knn_model.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    features = [request.form[f] for f in ['cap-shape', 'cap-surface', 'cap-color', 'bruises',
                                           'gill-attachment', 'gill-spacing', 'gill-color', 'stalk-shape',
                                           'stalk-color-above-ring', 'stalk-color-below-ring', 'ring-type',
                                           'population', 'habitat']]
    # Convert input to array format
    features = [int(f) for f in features]
    # Make prediction using the KNN model
    prediction = knn_model.predict([features])[0]
    # Determine the result message
    result = "Edible" if prediction == 0 else "Poisonous"
    return render_template('result.html', result=result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
