import pandas as pd
import glob

# read in gene table
genes = pd.read_csv("gene_range_table.txt", sep="\t", names = ["Gene_ID", "Chr", "Start", "End", "Name", "Synonym"])
genes = genes.drop(0, axis=0) # drop inital columns names
genes = genes.dropna() # drop NA
genes["bin"] = genes["Start"].astype(int) // 1e6 # binning
genes["gene_name"] = genes["Name"] # change column name
# genes.iloc[:, 2:4] = genes.iloc[:, 2:4].astype(int)
genes = genes[["gene_name", "bin"]] # slicing down to whats needed

# load all files and concatenate to one df,
all_files = glob.glob("*.cna.seg") # if files in folder: */*.cna.seg # todo folder change
li = []

for file in all_files:
    # read in file
    df = pd.read_csv(file, index_col = None, sep="\t")
    # print(df[["chr", "start", "end"]])
    id = file.replace(".cna.seg", "") # id name file[8:15] if in folders # todo folders
    df["ID"] = id # id column
    df["event"] = df[id + ".event"] # unique event column for merge
    df["bin"] = df["start"].astype(int) // 1e6 # binning
    df = df[["ID", "bin", "event"]] # slicing to what needed
    df = genes.merge(df, on="bin", how="inner")
    df = df.sort_values(by=["gene_name", "event"], ignore_index=True) # to keep gains and hetd at first position
    df = df.drop_duplicates(subset=["gene_name", "ID"], keep="first", ignore_index=True) # drop duplicates

    li.append(df[["gene_name", "ID", "event"]])
    print("Finished ID: ",id)

df = pd.concat(li, ignore_index=True)
# option for long format
# df = df.pivot(index = "gene_name" , columns = "ID", values = "event")
df.to_csv("genes_events_merge.csv")

# some useful functions for debugging
#
#
# print("Finished: Binning")
#
# # merge gene names to fragments
# df = genes.merge(df, on ="bin", how= "inner")
# df["gene_name"] = df["Name"]
# print("Finnished: Merge")
#
# df = df[["gene_name", "event", "ID"]]
# # print(df.isna().sum())
# # pivot from long to wide
# # cols = ["gene_name"] + list(df["ID"].unique())
#
# # print(len(df))
# # print(df.value_counts())
# # print(len(df.drop_duplicates()))
# # df = df.drop_duplicates(subset = ["gene_name", "ID"])
# #print(df.value_counts())
# # print(len(df.drop_duplicates(subset = ["gene_name", "ID"], keep = "first")))
#
# df = df.sort_values(by = ["gene_name", "event"], ignore_index=True)
# df = df.drop_duplicates(subset = ["gene_name", "ID"], keep = "first", ignore_index=True)
# print("Finished: Drop")
# # df = df.pivot(index = "gene_name" , columns = "ID", values = "event")
#
# # save to csv
# df.to_csv("genes_events_merge.csv")
# print("Finished: Exit code 0")