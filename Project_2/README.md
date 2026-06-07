# Project 2: Data Classification Using AI

## Overview

This project is a basic Artificial Intelligence classification project.  
The goal is to build a simple supervised machine learning model that can classify Iris flowers into different categories.

The model is trained using the Iris dataset. The dataset contains flower measurements such as:

- Sepal length
- Sepal width
- Petal length
- Petal width

Based on these measurements, the model predicts the flower class:

- Setosa
- Versicolor
- Virginica

## Project Objective

The main objective of this project is to understand the basic machine learning pipeline:

1. Load and understand a dataset
2. Split the dataset into training and testing sets
3. Apply feature scaling
4. Train a classification model
5. Make predictions
6. Evaluate the model using performance metrics

## Dataset Used

The Iris dataset is used in this project.

Dataset details:

- Total samples: 150
- Number of classes: 3
- Number of features: 4

The dataset is loaded directly from the `scikit-learn` library.

## Algorithm Used

The algorithm used in this project is:

**K-Nearest Neighbors (KNN)**

KNN is a simple classification algorithm.  
It predicts the class of a new data point by checking the nearest data points around it.

For example, if most of the nearest flowers are Setosa, the model predicts the new flower as Setosa.

## Libraries Used

The following Python libraries are used:

- pandas
- matplotlib
- scikit-learn

## Project Workflow

The project follows these steps:

1. Import required libraries
2. Load the Iris dataset
3. Convert the dataset into a pandas DataFrame
4. Explore and understand the dataset
5. Separate features and target labels
6. Split data into training and testing sets
7. Apply StandardScaler for feature scaling
8. Train the KNN classification model
9. Predict results on test data
10. Evaluate the model using:
   - Accuracy
   - F1 Score
   - Classification Report
   - Confusion Matrix
11. Test the model with new flower measurements
12. Compare different K values

## Model Evaluation

The model is evaluated using different metrics.

### Accuracy

Accuracy tells how many predictions were correct out of the total predictions.

### F1 Score

F1 Score gives a balanced measure of precision and recall.

### Confusion Matrix

The confusion matrix shows how many predictions were correct and where the model made mistakes.

## How to Run the Project

### Step 1: Install required libraries

```bash
pip install pandas matplotlib scikit-learn
