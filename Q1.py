import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

bins = [15, 26, 36, 51, 100]
labels = ["Youth", "Young Adults", "Adults", "Senior Citizens"]

df["Age Group"] = pd.cut(df["age"], bins=bins, labels=labels)

avg_usage = df.groupby("Age Group")["daily_screen_time_hours"].mean()

plt.bar(avg_usage.index, 
        avg_usage.values,
        color="skyblue", 
        edgecolor="black",
        alpha=0.7,
        width=0.6)

plt.xticks(rotation=30)
plt.title("Average Smartphone Usage by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Avg Screen Time")

plt.show()

sns.barplot(x="Age Group", y="daily_screen_time_hours", data=df)

plt.title("Average Smartphone Usage by Age Group")
plt.show()