import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

bins = [15, 26, 36, 51, 100]
labels = ["Youth", "Yo               ung Adults", "Adults", "Senior Citizens"]

df["Age Group"] = pd.cut(df["age"], bins=bins, labels=labels)

fig, axs = plt.subplots(2, 3, figsize=(15,7))
# Bar
sns.barplot(x="Age Group", y="daily_screen_time_hours", data=df, ax=axs[0,0], palette="viridis")
axs[0,0].set_title("Avg Usage by Age Group")
axs[0,0].tick_params(axis='x', rotation=20)

# Line
sns.lineplot(x="age", y="daily_screen_time_hours", data=df, ax=axs[0,1])
axs[0,1].set_title("Usage Trend by Age")

# Scatter
sns.scatterplot(x="daily_screen_time_hours", y="addicted_label",hue="addiction_level",data=df,ax=axs[0,2])
axs[0,2].set_title("Usage vs Addiction")

# Box
sns.boxplot(x="Age Group", y="daily_screen_time_hours", data=df, ax=axs[1,0],palette="Pastel1")
axs[1,0].set_title("Distribution (Box Plot)")
axs[1,0].tick_params(axis='x', rotation=20)

# Violin
sns.violinplot(x="Age Group", y="daily_screen_time_hours", data=df, ax=axs[1,1],palette="coolwarm")
axs[1,1].set_title("Density (Violin Plot)")
axs[1,1].tick_params(axis='x', rotation=20)
# Pie
counts = df["addiction_level"].value_counts()
axs[1,2].pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
axs[1,2].set_title("Addiction Distribution")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()