import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

sns.pairplot(
    df,
    hue="addiction_level",
    diag_kind="kde",
    palette="Set2",
    corner=True,
    height=2.5   # controls size of EACH subplot
)

plt.tight_layout()
plt.show()