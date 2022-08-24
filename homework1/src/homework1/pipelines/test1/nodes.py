import pandas as pd
import numpy as np

def gen_sample_df(cols):
    df = pd.DataFrame(abs(np.random.randn(100, 4))/10, columns=cols[1])
    df['CUS'] = np.random.randint(1, 999, size= (100, 1))
    df = df[['CUS'] + cols[1]]
    df.head()
    return df


def prepare_df(df, cols, meth):
    #scale, prepare
    return df


def calcClusterFact(df):
    # KMeans
    predict_labels, db_metric = 1,1
    return predict_labels, db_metric


def pca(df):
    # PCA decomp
    usr_df = df
    return usr_df