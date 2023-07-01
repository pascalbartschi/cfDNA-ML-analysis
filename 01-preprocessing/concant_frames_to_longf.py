import pandas as pd
import numpy as np
import seaborn as sns

def load_csv(path, file):
    data = pd.read_csv(path + file, sep=",")
    return data

def frame_dict(descriptions):

    path = "C:/Users/paesc/OneDrive/Dokumente/BSc_UZH/UZH_22HS/BME330_BK/BME_330_Python/fragment_lengths/"
    fl = "fragment_lengths_"
    ext = ".csv"
    # files = [fl + i + ext for i in descriptions]
    df_dict = {}

    for f in descriptions:
        frame = load_csv(path, fl + f + ext)
        frame = frame[(frame["length"] >= 101) & (frame["length"] <= 225)]
        frame = pd.melt(frame, id_vars= frame.columns[0], value_vars = frame.columns[1:])
        frame["Description"] = f
        frame.columns = ["length", "ID", "count", "type"]

        df_dict[f] = frame

    return df_dict


types = ["A", "B", "lung", "breast", "healthy"]
df_dict = frame_dict(types)

df_all = pd.concat([df_dict[key] for key in types])
df_all = df_all.set_index(df_all["length"])
df_all.to_csv("fragment_length_merged_longf.csv")

# todo cut al to some lengths





