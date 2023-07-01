import pandas as pd
import glob

# read in genes
genes = pd.read_csv("gene_range_table.txt", sep="\t", names = ["Gene_ID", "Chr", "Start", "End", "Name", "Synonym"])
genes = genes.drop(0, axis=0)
genes = genes.dropna()
genes.iloc[:, 2:4] = genes.iloc[:, 2:4].astype(int)

# load all files and concatenate to one df
all_files = glob.glob("*/*.cna.seg")
li = []


for file in all_files:
    df = pd.read_csv(file, index_col = None, sep="\t")
    id = file[8:15]
    df["ID"] = id
    df["event"] = df[id + ".event"]
    df = df[["ID", "chr", "start", "end", "event"]]
    li.append(df)
    print("Loaded ID: ",id)

df = pd.concat(li, ignore_index=True)


# binning
## add bin columns to files
df["bin"] = df["start"] // 1e6
genes["bin"] = genes["Start"] // 1e6

# merge gene names to fragments
df = genes.merge(df, on ="bin", how= "inner")
df["gene_name"] = df["Name"]

df = df[["gene_name", "event", "ID"]]
# print(df.isna().sum())
# pivot from long to wide
# cols = ["gene_name"] + list(df["ID"].unique())

# print(len(df))
# print(df.value_counts())
# print(len(df.drop_duplicates()))
# df = df.drop_duplicates(subset = ["gene_name", "ID"])
#print(df.value_counts())
# print(len(df.drop_duplicates(subset = ["gene_name", "ID"], keep = "first")))

df = df.sort_values(by = ["gene_name", "event"], ignore_index=True)
df = df.drop_duplicates(subset = ["gene_name", "ID"], keep = "first", ignore_index=True)
# df = df.pivot(index = "gene_name" , columns = "ID", values = "event")

# save to csv
df.to_csv("genes_events_merge.csv")