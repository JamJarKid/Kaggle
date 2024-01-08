import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import eda_functions, path_hacks

datapath = path_hacks.get_data_path(filepath=__file__, datafile='train.csv') 
train = pd.read_csv(datapath)

if __name__ == "__main__":
    pass
