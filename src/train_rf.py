import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import joblib


DATASET = "data/mobile_network_traffic.csv"

MODEL_PATH = "models/random_forest_model.pkl"


def load_dataset():

    df = pd.read_csv(DATASET)

    return df


def preprocess_data(df):

    X = df[
        [
            "Latency_ms",
            "Packet_Loss_%",
            "Signal_Strength_dBm",
            "Bandwidth_Utilization_%",
            "Active_Users"
        ]
    ]

    y = df["Traffic_Load_Mbps"]

    return X, y


def train_model(X_train, y_train):

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = mse ** 0.5

    r2 = r2_score(y_test, predictions)

    print("\n===== MODEL EVALUATION =====")

    print(f"MAE  : {mae:.2f}")

    print(f"RMSE : {rmse:.2f}")

    print(f"R2   : {r2:.2f}")

    return predictions


def save_model(model):

    joblib.dump(model, MODEL_PATH)

    print(f"\nModel saved to: {MODEL_PATH}")


def main():

    print("\nLoading Dataset...\n")

    df = load_dataset()

    print(df.head())

    X, y = preprocess_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("\nTraining Random Forest Model...\n")

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)

    save_model(model)


if __name__ == "__main__":

    main()
