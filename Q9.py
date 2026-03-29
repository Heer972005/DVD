import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")
df["addiction_level"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90
)

plt.title("Addiction Distribution")
plt.ylabel("")
plt.show()