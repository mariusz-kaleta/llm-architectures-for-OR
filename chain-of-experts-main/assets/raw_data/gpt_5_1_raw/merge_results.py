import pandas as pd

df_multi = pd.read_excel("experiment_summary.xlsx")
df_single = pd.read_excel("experiment_summary_1.xlsx")

print("multi shape:", df_multi.shape)
print("single shape:", df_single.shape)

df_all = pd.concat([df_multi, df_single], ignore_index=True)

df_all.to_excel("experiment_summary_merged.xlsx", index=False)

print("all shape:", df_all.shape)
