### 

rm(list = ls())

files <- list("EE87920_hist.csv",
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
        "EE88324_hist.csv")

file <- read.table(paste0("~/BSc_UZH/UZH_22HS/BME330_BK/BME_330_Python/hist_data/", files[[1]]),
           quote="\"",
           comment.char="")



