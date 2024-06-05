import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    # Load prepared data
    data = pd.read_csv('data/prepared_data.csv')

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop('Country', axis=1), data['Country'], test_size=0.2, random_state=42)

    X_test.to_csv('data/test_data.csv')


    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, '/data/model.joblib')

if __name__ == "__main__":
    train_model()
