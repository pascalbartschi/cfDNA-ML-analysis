import numpy as np
import pandas as pd

names = ["ID", "tumour_fraction", "ploidy", "gender"]
df_A = pd.read_csv("ichor_CNA/tumourfraction_A.tsv", sep="\t", names = names)
df_B = pd.read_csv("ichor_CNA/tumourfraction_B.tsv", sep="\t", names = names)
df_C = pd.read_csv("ichor_CNA/tumourfractions_C.tsv", sep="\t", names = names)
df_wadu = pd.read_csv("ichor_CNA/tumourfractions_lung_breast_healthy.tsv", sep="\t", names = names)
df_meta = pd.read_csv("ichor_CNA/metadata_all.csv", names = ["ID", "type"])


dfs = {"A": df_A,
       "B": df_B,
       "C": df_C,
       "rest": df_wadu}


for key in dfs.keys():
    dfs[key] = dfs[key].drop(0, axis=0)
    dfs[key] = dfs[key].iloc[::6, :]
    dfs[key] = dfs[key].set_index("ID")

df_all = pd.concat([dfs[key] for key in dfs.keys()], ignore_index=False)
df_meta.set_index("ID")

df_all = df_all.merge(df_meta, on="ID", how="inner")
# df_all = df_all.sort_values(by = "ID", axis = 0)

df_all.to_csv("ichor_CNA/ichor_CNA_tumours_fractions_all.csv", encoding = "utf-8")





# df = df.iloc[::6, :] # drop reduncant rows

