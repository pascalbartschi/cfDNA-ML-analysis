import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(path, file):

    data = pd.read_csv(path + file, names = ["length", "count"], sep = "\s+")
    data = data.set_index(data["length"])
    data = data.drop(labels="length", axis=1)

    return data

def merge_data(path,files, how  ="inner"):

    data = load_data(path, files[0])

    for file in files[1:]:

        data1 = load_data(path, file)

        data = data.merge(data1, on='length', how = how)

    data.columns = [file.replace("_lenuniqcount.tsv", "") for file in files]

    return data

def convert_tsv_to_csv(path, file):
    data = pd.read_csv(path + file, sep = "\t")

    return data


breast_cancer = ["EE" + str(i) + "_lenuniqcount.tsv" for i in range(87811, 87864+1)]
del breast_cancer[3]
lung_cancer = ["EE" + str(i) + "_lenuniqcount.tsv" for i in range(88183, 88261 + 1)]

path = "C:/Users/paesc/OneDrive/Dokumente/BSc_UZH/UZH_22HS/BME330_BK/tumour_samples/tumour_samples/"

breast = merge_data(path, breast_cancer)
# breast = breast[(breast.index >= 98) & (breast.index <= 230)]
lung = merge_data(path, lung_cancer)
# lung = lung[(lung.index >= 98) & (lung.index <= 230)]
#
# breast.to_csv("fragment_lengths_breast.csv")
# lung.to_csv("fragment_lengths_lung.csv")

path2 = "C:/Users/paesc/OneDrive/Dokumente/BSc_UZH/UZH_22HS/BME330_BK/BME_330_Python/hist_data_healthy/"
file2 = "uniqcounts90_240.tsv"

healthy = convert_tsv_to_csv(path2, file2)
healthy = healthy.set_index(healthy["length"])
# healthy = healthy[(healthy.index >= 98) & (healthy.index <= 230)]
#healthy.to_csv("fragment_lengths_healthy.csv")

dropout_range = "mode not in 100 to 171"



