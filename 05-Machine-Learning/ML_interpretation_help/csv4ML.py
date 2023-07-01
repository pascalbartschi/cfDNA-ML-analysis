import pandas as pd

# load data
samplemap = pd.read_csv("samplemap.tsv", sep="\t")
tumour_fractions = pd.read_csv("ichor_CNA_tumours_fractions_all.csv")
fragment_features = pd.read_csv("fragment_lengths_all.tsv", sep="\t")
cell_type_signature = pd.read_csv("summary_across_samples_and_ROIS.csv")


# drop unnecessary
fragment_features.dropna(inplace = True)
tumour_fractions.drop("Unnamed: 0", axis = 1, inplace = True)
tumour_fractions = tumour_fractions[["ID", "tumour_fraction", "ploidy", "gender"]]
cell_type_signature = cell_type_signature[["sample", "region-set", "Dip area: z-score vs controls in same region set", "Dip depth: z-score vs controls in same region set"]]


# wide to long
fragment_features = pd.melt(fragment_features,
                            id_vars = "length",
                            var_name = "sample",
                            value_name = "count")


# to obtain proper csv without unnecessary columns
tumour_fractions.columns = ["sample", "tf", "ploidy", "gender"]
cell_type_signature.columns = ["sample", "region_set", "Dip_area", "Dip_depth"]

# merge cell_signatures with ROIS
ROIS = ["A549_hg38",
        "HPF_lung_fibroblast_cluster1737_hg38",
        "HeLa_cluster1777_hg38",
        "SAEC_hg38",
        "colon_cluster507_hg38",
        "hematopoietic_specific_liquorice_hg38",
        "hepatocyte_all_hg38",
        "melano_SOX_clusters1863_2205_hg38",
        "panc_adenoca_cluster1261_hg38",
        "panc_epithel_cluster1974_hg38",
        "prostate_cluster2483_hg38",
        "skeletal_muscle_cluster1518_hg38",
        "mammary_epithel_cluster2438_hg38"]
ROIS = pd.DataFrame({"region_set": ROIS})
cell_type_signature = cell_type_signature.merge(ROIS, on = "region_set", how="inner")


samplemap.set_index("sample", inplace = True)
tumour_fractions.set_index("sample", inplace = True)
fragment_features.set_index("sample", inplace = True)
cell_type_signature.set_index("sample", inplace = True)


# save to csv
samplemap.to_csv("Machine_Learning/sample_map_ML.csv")
tumour_fractions.to_csv("Machine_Learning/tumour_fractions_ML.csv")
fragment_features.to_csv("Machine_Learning/fragment_features_CNA_ML.csv")
cell_type_signature.to_csv("Machine_Learning/cell_type_signatures_LIQU_ML.csv")

