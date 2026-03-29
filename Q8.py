import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")
bins=[15, 26, 36, 51, 100]
labels = ["Youth", "Young Adults", "Adults", "Senior Citizens"]
df["Age Group"]=pd.cut(df["age"],bins=bins,labels=labels)
group = df.groupby("Age Group")[[
    "social_media_hours",
    "gaming_hours"
]].sum()

plt.stackplot(group.index,
              group["social_media_hours"],
              group["gaming_hours"],
              labels=["Social Media", "Gaming"],
              alpha=0.8)

plt.title("Contribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Hours")
plt.show()