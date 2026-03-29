import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

bins = [15, 25, 35, 50, 100]
labels = ["Youth", "Young Adults", "Adults", "Senior Citizens"]

df["Age Group"] = pd.cut(df["age"], bins=bins, labels=labels)

fig, axs = plt.subplots(2, 3, figsize=(15,10))
# Bar
sns.barplot(x="Age Group", y="daily_screen_time_hours", data=df, ax=axs[0,0])

# Line
sns.lineplot(x="age", y="daily_screen_time_hours", data=df, ax=axs[0,1])

# Scatter
sns.scatterplot(x="daily_screen_time_hours", y="weekend_screen_time", data=df, ax=axs[0,2])

# Box
sns.boxplot(x="Age Group", y="daily_screen_time_hours", data=df, ax=axs[1,0])

# Violin
sns.violinplot(x="Age Group", y="daily_screen_time_hours", data=df, ax=axs[1,1])

# Pie
df["addiction_level"].value_counts().plot(kind="pie", ax=axs[1,2])

plt.tight_layout()
plt.show()