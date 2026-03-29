import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

age_usage = df.groupby("age")["daily_screen_time_hours"].mean()

plt.plot(age_usage.index, age_usage.values, marker='o')
plt.title("Usage Trend by Age")
plt.show()

sns.lineplot(x="age", y="daily_screen_time_hours", data=df)

plt.title("Usage Trend")
plt.show()