import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

plt.scatter(
    df["daily_screen_time_hours"], 
    df["addicted_label"], 
    alpha=0.5,
    color="blue")

plt.title("Usage vs Addiction")
plt.xlabel("Daily Screen Time")
plt.ylabel("Weekend Screen Time")
plt.grid(alpha=0.4)
plt.show()


sns.scatterplot(x="daily_screen_time_hours",
                 y="addicted_label", 
                 hue="addiction_level", 
                 data=df,
                 alpha=0.6)
plt.title("Usage vs Addiction Level")
plt.xlabel("Daily Screen Time")
plt.ylabel("Addicted Label")
plt.show()