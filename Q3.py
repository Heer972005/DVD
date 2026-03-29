import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

age_usage = df.groupby("age")["daily_screen_time_hours"].mean()

plt.plot(age_usage.index, 
         age_usage.values, 
         marker='o',
         linestyle='--',
         linewidth=2,
         color="blue"
         )
plt.title("Usage Trend by Age")
plt.xlabel("Age")
plt.ylabel("Average Screen Time (hours)")
plt.grid(alpha=0.5)
plt.show()

sns.lineplot(x=age_usage.index,
    y=age_usage.values,
    marker='o',
    linewidth=2)

plt.title("Usage Trend")
plt.xlabel("Age")
plt.ylabel("Average Screen Time (hours)")
plt.show()