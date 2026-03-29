import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

plt.scatter(df["daily_screen_time_hours"], df["weekend_screen_time"], alpha=0.5)

plt.xlabel("Daily Screen Time")
plt.ylabel("Weekend Screen Time")
plt.show()

sns.scatterplot(x="daily_screen_time_hours", y="weekend_screen_time", hue="addiction_level", data=df)

plt.show()