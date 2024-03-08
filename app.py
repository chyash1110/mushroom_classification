from flask import Flask, render_template, request
import joblib

knn_model = joblib.load('knn_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [request.form[f] for f in ['cap-shape', 'cap-surface', 'cap-color', 'bruises',
                                           'gill-attachment', 'gill-spacing', 'gill-color', 'stalk-shape',
                                           'stalk-color-above-ring', 'stalk-color-below-ring', 'ring-type',
                                           'population', 'habitat']]

    features = [int(f) for f in features]
    prediction = knn_model.predict([features])[0]
    result = "Edible" if prediction == 0 else "Poisonous"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
