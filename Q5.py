import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

bins = [15, 25, 35, 50, 100]
labels = ["Youth", "Young Adults", "Adults", "Senior Citizens"]

df["Age Group"] = pd.cut(df["age"], bins=bins, labels=labels)

grouped = df.groupby("Age Group", observed=True)

groups = []
labels = []

for name, group in grouped:
    groups.append(group["daily_screen_time_hours"].values)
    labels.append(name)

plt.boxplot(groups, tick_labels=labels)

plt.title("Box Plot of Usage by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Screen Time")

plt.show()

sns.boxplot(x="Age Group", y="daily_screen_time_hours", data=df)

plt.show()