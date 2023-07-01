import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # concatenate separate files and store in csv
#
# all_files = glob.glob("oncogenes/*.csv")
# # load files and concatenate
# df = pd.concat([pd.read_csv(file) for file in all_files[:-1]], ignore_index=True) # concatenate to one frame
# df = df.drop("Unnamed: 0", axis = 1)
# # load metadata
# meta = pd.read_csv(all_files[-1], names = ["ID", "class"])
# # merge with metadata
# df = df.merge(meta, on = "ID", how="inner")
# df = df.set_index("gene_name")
# df.to_csv("cancer_CNA/genes_events_meta_merge.csv")

# merge with cancer_CNA data

# df = pd.read_csv("cancer_CNA/genes_events_meta_merge.csv")
# all_files = glob.glob("cancer_CNA/*cancerCNA.csv")
# df_cna = pd.concat([pd.read_csv(file) for file in all_files], ignore_index=True) # concatenate to one frame
# df_cna.columns = ["gene_name", "type", "cna"]
# df_merged = df.merge(df_cna, on = "gene_name", how= "inner")
# df_cancer = df_merged[df_merged["event"] != "NEUT"]
# df_cancer.columns = ['gene_name', 'ID', 'event', 'origin', 'type', 'cna']
# df_cancer = df_cancer.set_index("gene_name")
#
# df_cancer.to_csv("df_cancer.csv")


def stats(df_cancer):

    norm_counts = df_cancer.groupby(by=["origin"])["type"].count() / \
                  df_cancer.groupby(by=["origin", "ID"])["ID"].unique().groupby(by="origin").count()

    # gene counts (normalized) for every type per origin
    type_counts = df_cancer.groupby(by=["origin", "type"])["type"].count()

    type_norm_counts = df_cancer.groupby(by=["origin", "type"])["type"].count() / \
                  df_cancer.groupby(by=["origin"])["type"].count()

    gene_occ = df_cancer.groupby(by=["gene_name", "type"])["type"].count()

    return norm_counts, type_counts, type_norm_counts, gene_occ

def shared_gen(df_cancer):
    genes1 = df_cancer.groupby(by = ["type"])["gene_name"].unique()
    genes = []
    for sub in genes1:
        genes = genes + list(sub)
    print(len(genes))
    shared_genes = []
    for i in range(len(genes)):
        if genes[i] in genes[i+1:]:
            shared_genes.append(genes[i])
    print(len(shared_genes))

    return list(pd.Series(sorted(shared_genes)).unique()) # pd.DataFrame({"gene_name": shared_genes})


    # types = df_cancer.type.unique()
    # gene_frame = {}
    # for i in range(len(genes)):
    #     gene_frame[types[i]] = pd.DataFrame({types[i]: genes[i]})


    # unique_genes = gene_frame["bile"]
    # for key in list(gene_frame.keys())[1:]:
    #     unique_genes = unique_genes.join(gene_frame[key])


    #return unique_genes

# read in files

TF = pd.read_csv("ichor_CNA_tumours_fractions_all.csv", sep=",")
TF = TF.drop("Unnamed: 0", axis = 1)
TF.columns = ["ID", "tf", "ploidy", "gender", "origin"]
TF = TF[["ID", "tf", "gender"]]

df_cancer = pd.read_csv("df_cancer.csv")

# drop rows with shared genes
shared_genes = shared_gen(df_cancer)
df_cancer = df_cancer[~df_cancer["gene_name"].isin(shared_genes)]
df_cancer = df_cancer.merge(TF, on = "ID", how = "inner")
df_highTF = df_cancer[df_cancer["tf"] >= 0.03]

norm_counts, type_counts, type_norm_counts, gene_occ = stats(df_cancer)

norm_counts_tf, type_counts_tf, type_norm_counts_tf, gene_occ_tf = stats(df_highTF)

# u = unique_genes["bile"].join(unique_genes["pancreas"]) # join
# unique_genes["pancreas"].compare(unique_genes["bile"]) # compare

# only look at high tumour fraction samples
# compare to healthy
# unique genes