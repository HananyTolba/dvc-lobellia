import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

def validate_model():
    # Load test data
    X_test = pd.read_csv('data/test_data.csv')

    # Load model
    model = joblib.load('/data/model.joblib')

    # Predict
    predictions = model.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, predictions)
    print(f'Accuracy: {accuracy}')

if __name__ == "__main__":
    validate_model()
