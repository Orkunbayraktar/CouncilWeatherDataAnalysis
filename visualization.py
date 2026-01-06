import matplotlib.pyplot as plt
import seaborn as sns

def visualize(df):
    # Line plot
    plt.figure()
    plt.plot(df["date"], df["temperature"])
    plt.title("Daily Temperature")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Box plot
    plt.figure()
    sns.boxplot(y=df["temperature"])
    plt.title("Temperature Distribution")
    plt.show()

    # Anomaly visualization
    plt.figure()
    sns.scatterplot(
        x=df["date"],
        y=df["temperature"],
        hue=df["anomaly"]
    )
    plt.title("Temperature Anomalies")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
