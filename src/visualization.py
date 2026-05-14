import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


DATASET = "data/mobile_network_traffic.csv"


def load_dataset():

    df = pd.read_csv(DATASET)

    return df


def prepare_data(df):

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


def plot_actual_vs_predicted(y_test, predictions):

    plt.figure(figsize=(10, 5))

    plt.plot(
        y_test.values,
        label="Actual Traffic"
    )

    plt.plot(
        predictions,
        label="Predicted Traffic"
    )

    plt.title("Actual vs Predicted Traffic")

    plt.xlabel("Samples")

    plt.ylabel("Traffic Load (Mbps)")

    plt.legend()

    plt.grid(True)

    plt.savefig(
        "outputs/graphs/actual_vs_predicted.png"
    )

    plt.show()


def plot_traffic_trend(df):

    plt.figure(figsize=(10, 5))

    plt.plot(df["Traffic_Load_Mbps"])

    plt.title("Traffic Load Trend")

    plt.xlabel("Samples")

    plt.ylabel("Traffic Load (Mbps)")

    plt.grid(True)

    plt.savefig(
        "outputs/graphs/traffic_trend.png"
    )

    plt.show()


def main():

    print("\nLoading Dataset...\n")

    df = load_dataset()

    X, y = prepare_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("\nTraining Model...\n")

    model = train_model(X_train, y_train)

    predictions = model.predict(X_test)

    print("\nGenerating Graphs...\n")

    plot_actual_vs_predicted(
        y_test,
        predictions
    )

    plot_traffic_trend(df)

    print("\nGraphs Saved Successfully!\n")


if __name__ == "__main__":

    main()
