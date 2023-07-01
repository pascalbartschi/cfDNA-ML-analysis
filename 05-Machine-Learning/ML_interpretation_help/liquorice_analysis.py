import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# meta = pd.read_csv("metadata_all.csv", sep = ",", names = ["ID", "origin"])
# result = pd.read_csv("summary_across_samples_and_ROIS.csv", sep=",")
# result = result[["sample",
#                  "region-set",
#                  "Dip depth: z-score vs controls in same region set"]]
# result.columns = ["ID", "region_set", "dip_depth: z vs. control"] # region set is cell type
# TF = pd.read_csv("ichor_CNA_tumours_fractions_all.csv", sep=",")
# TF = TF[["ID", "tumour_fraction"]]
#
# result = result.merge(meta, on = "ID", how = "inner")
# result = result.merge(TF, on = "ID", how = "inner")
# result = result.set_index("ID")
#
# result.to_csv("liquorice_output_analysis.csv")

df = pd.read_csv("liquorice_output_analysis.csv")
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
df = df.merge(ROIS, on = "region_set", how="inner")
df.columns = ['ID', 'region_set', 'depth', 'origin', 'TF']

sns.set(font_scale = 5)

# plot unfiltered

plt.figure(figsize = (50,50), layout = "tight")
sns.boxplot(df, x = "depth", y = "region_set", hue = "origin")
plt.xlim(-10, 10)
plt.title("High TF: Dip depth of ROI and origin")
plt.savefig("boxplots/boxplot_liquorice_analysis.png", dpi = 300)
plt.clf()

# frame filtered for tumour fractions with different lims
lims = [0.01, 0.02, 0.03]

for lim in lims:
        df_healthy = df[df["origin"] == "Healthy"]
        df_healthy = df_healthy[df_healthy["TF"] < lim]
        df_other = df[df["origin"] != "Healthy"]
        df_highTF = df_other[df_other["TF"] >= lim] # only IDs with tumour fraction higher than 3%
        df_highTF = pd.concat([df_highTF, df_healthy])


        plt.figure(figsize = (50,50), layout = "tight")
        sns.boxplot(df_highTF, x = "depth", y = "region_set", hue = "origin")
        plt.xlim(-10, 10)
        plt.title("High TF: Dip depth of ROI and origin, lim = " + str(lim))
        plt.savefig("boxplots/boxplot_liquorice_analysis_highTF_lim=" + str(lim) + ".png", dpi = 300)
        plt.clf()









