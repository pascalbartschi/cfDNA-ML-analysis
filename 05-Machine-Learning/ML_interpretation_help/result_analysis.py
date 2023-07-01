import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sm = pd.read_csv("Machine_Learning/sample_map_ML.csv")
tf = pd.read_csv("Machine_Learning/tumour_fractions_ML.csv")
ff = pd.read_csv("Machine_Learning/fragment_features_CNA_ML.csv")
cs = pd.read_csv("Machine_Learning/cell_type_signatures_LIQU_ML.csv")

palette = sns.color_palette(palette = ["red", "orange", "#0b5394", "#3d85c6", "#20124d",  "green"])

def norm(df):
    df["norm_count"] = df["count"] / df["count"].sum()
    df["sample_mode"] = df["norm_count"].median()

    return df

def over150ratio(df):
    df["ratio"] = df[df["length"] < 150]["count"].sum() / df["count"].sum()

    return df

# set style

sns.set_theme(font_scale=3, style = "whitegrid", palette = palette)

# length features
# distribution plot of cancer vs. healthy # todo normalize counts

ff = ff.merge(sm, on = "sample", how = "inner") # todo drop outliers
ff = ff.groupby(by="sample").apply(norm)
ff = ff.groupby(by="sample").apply(over150ratio)
# drop outliers
ff = ff[ff["sample"] != "EE87920"]
ff = ff[ff["sample"] != "EE87921"]
# distribution plot with all samples
plt.figure(figsize=(20, 20))
sns.lineplot(data=ff, x="length", y="norm_count", hue="diagnosis", units="sample", estimator=None,
             hue_order=["Lung", "Breast", "A" ,"B", "C", "Healthy"])

plt.title("Distribution of normalized fragment lengths")
plt.xlabel("Length [bp]")
plt.ylabel("Normalized count")
plt.savefig("ff_figures/fragment_length_distribution.png", dpi = 300)
plt.show()
plt.clf()

# boxplot plot of cancer vs. healthy

# binary than length binning
ff1 = ff[ff.diagnosis == "Healthy"].copy()
ff1["type"] = "Healthy"
ff2 = ff[ff.diagnosis != "Healthy"].copy()
ff2["type"] = "Cancer"
ff = pd.concat([ff1, ff2])
# ff["l_bin"] = ff["length"] // 20

plt.figure(figsize = (30,10))
sns.boxplot(data = ff, x = "diagnosis", y = "ratio", order = ["Lung", "Breast", "A" ,"B", "C", "Healthy"],
            showfliers = False)
plt.title("Ratios of counts with length <150 per diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Length <150 ratio")
plt.savefig("ff_figures/box_plot_norm_counts", dpi = 300)
plt.show()
plt.clf()


# tumour fraction estimates boxplot
# merge with diagnosis and construct binary column
tf = tf.merge(sm, on = "sample", how = "inner")
tf1 = tf[tf.diagnosis == "Healthy"].copy()
tf1["type"] = "Healthy"
tf2 = tf[tf.diagnosis != "Healthy"].copy()
tf2["type"] = "Cancer"
tf = pd.concat([tf1, tf2])
tf["tf_percent"] = tf["tf"] * 100

plt.figure(figsize = (30, 15))
sns.boxplot(data = tf, x = "diagnosis", y = "tf", order = ["Lung", "Breast", "A" ,"B", "C", "Healthy"], showfliers = False)
plt.ylim(0, 0.10)
plt.title("Tumour fractions of diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Tumour fraction")
plt.savefig("tf_figures/boxplot_diagnosis_tf.png", dpi = 300)
plt.show()
plt.clf()

plt.figure(figsize = (30, 10))
sns.boxplot(data = tf, x = "diagnosis", y = "tf", hue = "gender", palette = ["grey", "black"], showfliers = False)
plt.ylim(0, 0.10)
plt.title("Tumour fractions in gender")
plt.xlabel("Diagnosis")
plt.ylabel("Tumour fraction")
plt.savefig("tf_figures/boxplot_diagnosis_gender_tf.png", dpi = 300)
plt.show()
plt.clf()


# plots for cell type signatures
cs = cs.merge(sm, on = "sample", how = "inner")


for signature in cs.region_set.unique():
    local = cs[cs["region_set"] == signature]
    # # boxplot area
    # plt.figure(figsize = (30,15))
    # sns.boxplot(data = local, x = "diagnosis", y = "Dip_area", order=["Lung", "Breast", "A" ,"B", "C", "Healthy"])
    # plt.title(signature + " dip area")
    # plt.xlabel("Diagnosis")
    # plt.ylabel("Dip area")
    # plt.savefig("cs_figures/" + signature + "_AREA.png", dpi = 300)
    # plt.show()
    # plt.clf()
    # boxplot depth
    plt.figure(figsize=(30, 15))
    sns.boxplot(data=local, x="diagnosis", y="Dip_depth", order=["Lung", "Breast", "A" ,"B", "C", "Healthy"], showfliers = False)
    plt.title(signature + " dip depth")
    plt.xlabel("Diagnosis")
    plt.ylabel("Dip depth")
    plt.savefig("cs_figures/" + signature + "_DEPTH.png", dpi = 300)
    # plt.show()
    plt.clf()