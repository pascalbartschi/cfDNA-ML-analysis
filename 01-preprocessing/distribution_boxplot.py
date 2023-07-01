import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file = "C:/Users/paesc/OneDrive/Dokumente/BSc_UZH/UZH_22HS/BME330_BK/BME_330_Python/" \
       "fragment_length_merged_longf.csv"

df = pd.read_csv(file, sep= ",")
df = df.drop("length.1", axis = 1)
# sums = df.groupby(by="ID").sum().iloc[:,1]

def norm(df):
    df["norm_count"] = df["count"] / df["count"].sum()
    df["sample_mode"] = df["norm_count"].median()

    return df

def stats(df):
    df["length_std"] = df["norm_count"].std()
    df["length_mean"] = df["norm_count"].mean()

    return df


def debubg_norm():
    zeros = []
    for id, group in df_norm.groupby("ID"):
        x = df_norm[df_norm["ID"] == id]["norm_count"].sum()
        print(x)
        if x < 0.99:
            zeros.append(id)
    return zeros


def plot(df):

    # plt.figure(figsize = (20,20))
    # sns.boxplot(data=df_norm,x="length_mean", y = "type")
    # plt.title("Boxplot")
    # plt.savefig("figures/boxplot.png")
    # plt.show()
    # plt.clf()

    # distribution plot with all samples
    plt.figure(figsize = (20,20))
    sns.lineplot(data=df_norm, x="length", y="norm_count", hue="type",units="ID", estimator = None,
                 hue_order= ["healthy", "lung", "breast", "B", "A"])
    plt.title("Sample distribution")
    plt.savefig("figures/distribution_samples_plot.png")
    plt.show()
    plt.clf()

    # # distribution plot means all samples
    # plt.figure(figsize=(20, 20))
    # sns.lineplot(data=df_norm, x="length", y="length_mean", hue="type", units="ID", estimator=None,
    #              hue_order=["healthy", "lung", "breast", "B", "A"])
    # # plt.plot(df["length"], df["count"], color=df["type"])
    # plt.title("Mean distribution")
    # plt.savefig("figures/distribution_mean_plot.png")
    # plt.show()
    # plt.clf()

def density_df(df):
    '''ends after i die due to nested loop'''

    local = pd.DataFrame({"lengths": [], "type": []})

    # types = ["A", "B", "lung", "breast", "healthy"]
    # for type in types:
    #     print(type)
    #     sub_df = df[df["type"] == type]
    #     for index in sub_df.index:
    #         for i in range(int(sub_df.iloc[int(index), 2])):
    #             # print(sub_df.iloc[int(index), 0], type)
    #             d_row = pd.DataFrame({"lengths": sub_df.iloc[int(index), 0], "type": type}, index=[0])
    #             local = pd.concat([local, d_row], ignore_index=True)

    return local








df_norm = df.groupby(by="ID").apply(norm)

df_norm = df_norm.groupby(by="length").apply(stats)

df_norm = df_norm[df_norm["ID"]!="length.1"] # some intruder in df

# df_dens = density_df(df)
# total_counts of one length per type = int(len(df[(df["type"] == "A") & (df["length"] == 191)]) * df["count"].sum())


# plt.figure()
# sns.kdeplot(data = df ,x = "densitiy_length",  hue = "type" )
# plt.savefig("kdeplot.png")
# plt.show()
# plt.clf()
# plot()
# df_norm.to_csv("debug_df_norm.csv")

plt.figure(figsize = (10, 10))
plt.clf()




