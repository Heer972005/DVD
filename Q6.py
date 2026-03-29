import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")
bins = [15, 25, 35, 50, 100]
labels = ["Youth", "Young Adults", "Adults", "Senior Citizens"]

df["Age Group"] = pd.cut(df["age"], bins=bins, labels=labels)

sns.violinplot(x="Age Group", y="daily_screen_time_hours", data=df)

plt.title("Violin Plot")
plt.show()