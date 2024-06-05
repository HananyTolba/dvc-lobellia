import pandas as pd




def prepare_data():
    # Load data
    data = pd.read_csv("data/customers-100000.txt")

    # Preprocessing steps
    # ...

    # Save prepared data
    data.to_csv('data/prepared_data.csv', index=False)

if __name__ == "__main__":
    prepare_data()
