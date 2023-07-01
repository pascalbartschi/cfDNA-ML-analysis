import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(path, file):

    data = pd.read_csv(path + file, sep = '\s+',
                       names=["count", "length"])
    data = data[data['length'] >= 0]
    data = data.sort_values("length")
    data = data.set_index(data["length"])
    data = data.drop(labels = "length", axis = 1)

    return data

def merge_data(files, how = 'inner'):

    path = "C:/Users/paesc/OneDrive/Dokumente/BSc_UZH/UZH_22HS/BME330_BK/BME_330_Python/hist_data/"

    data = load_data(path, files[0])

    for file in files[1:]:

        data1 = load_data(path, file)

        data = data.merge(data1, on='length', how = how)

    data.columns = [file.replace("_hist.csv", "") for file in files]
    return data

def files():

    path = "C:/Users/paesc/OneDrive/Dokumente/BSc_UZH/UZH_22HS/BME330_BK/BME_330_Python/hist_data/"

    files = [# "EE87920_hist.csv", # healthy
            "EE88290_hist.csv",
            "EE88291_hist.csv",
            "EE88292_hist.csv",
            "EE88293_hist.csv",
            "EE88294_hist.csv",
            "EE88295_hist.csv",
            "EE88296_hist.csv",
            "EE88297_hist.csv",
            "EE88298_hist.csv",
            "EE88299_hist.csv",
            "EE88301_hist.csv",
            "EE88302_hist.csv",
            "EE88303_hist.csv",
            "EE88304_hist.csv",
            "EE88305_hist.csv",
            "EE88306_hist.csv",
            "EE88307_hist.csv",
            "EE88308_hist.csv",
            "EE88309_hist.csv",
            "EE88310_hist.csv",
            "EE88311_hist.csv",
            "EE88312_hist.csv",
            "EE88313_hist.csv",
            "EE88314_hist.csv",
            "EE88315_hist.csv",
            "EE88316_hist.csv",
            "EE88317_hist.csv",
            "EE88318_hist.csv",
            "EE88319_hist.csv",
            "EE88320_hist.csv",
            "EE88321_hist.csv",
            "EE88322_hist.csv",
            "EE88323_hist.csv",
            "EE88324_hist.csv"]

    return files, path

def plot_CDF(data):

    plt.figure(figsize = (20,20))
    for i, col in enumerate(list(data)):
        plt.plot(data.index, data.iloc[:,i], label=col)

    plt.legend(loc="upper right")
    plt.title("cfDNA length distributions", size = 20)
    plt.savefig("cfDNA_length_distributions.png", dpi = 350)
    plt.show()

if __name__ == "__main__":

    data = merge_data(files()[0]) # we lost very short and very long fragment through argument "inner"
    data.to_csv("Fragment_length.csv", encoding = "utf-8")
    plot_CDF(data)

# dataframe should be extended with healthy, A, B, lung, breast




# healthy = pd.read_csv()






