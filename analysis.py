import pandas as pd

def statistical_summary(df):
    print("Mean temperature:", df["temperature"].mean())
    print("Min temperature:", df["temperature"].min())
    print("Max temperature:", df["temperature"].max())
    print("\nQuartiles:")
    print(df["temperature"].quantile([0.25, 0.5, 0.75]))

def detect_anomalies(df):
    df["rolling_avg"] = df["temperature"].rolling(window=3).mean()

    mean = df["temperature"].mean()
    std = df["temperature"].std()

    anomaly_flags = []

    for temp in df["temperature"]:
        if temp > mean + 2 * std:
            anomaly_flags.append("High anomaly")
        elif temp < mean - 2 * std:
            anomaly_flags.append("Low anomaly")
        else:
            anomaly_flags.append("Normal")

    df["anomaly"] = anomaly_flags
    return df
