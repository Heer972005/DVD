import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")
counts=df["addiction_level"].value_counts()

explode = [0.05] * len(counts)   # slight explosion

colors = ["#ff9999", "#66b3ff", "#99ff99"]

plt.pie(
    counts,
    labels=counts.index,
    autopct="%1.1f%%",
    startangle=90,
    explode=explode,
    colors=colors
)

plt.title("Addiction Distribution")
plt.show()