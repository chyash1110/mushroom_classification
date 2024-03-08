# Mushroom Classification Web App

This project is aimed at classifying mushrooms into edible or poisonous categories using machine learning algorithms. It includes a Jupyter Notebook for data preprocessing, model training, and evaluation, as well as a Flask web application for real-time classification.

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Dataset](#dataset)
- [Usage](#usage)
- [Model Evaluation](#model-evaluation)
- [Web Application](#web-application)
- [License](#license)

## Introduction

Mushrooms are an essential part of many cuisines worldwide, but identifying whether a mushroom is safe to eat or poisonous can be challenging. This project aims to provide a solution by leveraging machine learning techniques to classify mushrooms into edible or poisonous categories based on various features.

## Dependencies

To run the Jupyter Notebook and the Flask web application, you need the following dependencies:

- Python 3.x
- Jupyter Notebook
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn
- Flask

You can install these dependencies using pip:

```
pip install jupyter pandas numpy seaborn matplotlib scikit-learn flask
```

## Dataset

The dataset used in this project contains various attributes of mushrooms such as cap shape, cap surface, gill color, etc., along with their classifications as edible or poisonous.

## Usage

1. Clone the repository:

```
git clone https://github.com/chyash1110/mushroom_classification
cd mushroom-classification
```

2. Run the Jupyter Notebook:

```
jupyter notebook mushroom.ipynb
```

3. Follow the instructions in the notebook for data preprocessing, model training, and evaluation.

4. Run the Flask web application:

```
python app.py
```

5. Open a web browser and go to `http://localhost:5000` to access the web application.

## Model Evaluation

The notebook includes evaluations of three machine learning models:

- Logistic Regression
- Gaussian Naive Bayes
- K-Nearest Neighbors (KNN)

Evaluation metrics such as accuracy, precision, recall, and F1-score are provided for each model.

## Web Application

The Flask web application allows users to classify mushrooms in real-time. Users can input various features of the mushroom, and the application will predict whether it is edible or poisonous using the KNN model trained in the notebook.
