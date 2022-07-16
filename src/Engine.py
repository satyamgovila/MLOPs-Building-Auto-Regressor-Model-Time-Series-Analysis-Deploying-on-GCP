import pandas as pd
import seaborn as sns
sns.set()

from ML_Pipeline.WhiteNoise import WhiteNoise
from ML_Pipeline.Preprocess import Preprocess
from ML_Pipeline.AcfAndPacf import AcfAndPcf
from ML_Pipeline.Autoregressor import Autoregressor
from ML_Pipeline.RandomWalk import RandomWalk
from ML_Pipeline.RollingWindow import RollingWindow
from ML_Pipeline.Stationarity import Stationarity

def run():
    # importing the data
    raw_csv_data = pd.read_csv("../input/Data-Chillers.csv") #read the data

    df_comp = raw_csv_data.copy()     # create a copy

    # Preprocess
    prep = Preprocess(df_comp)     

    # White noise
    wnoise = WhiteNoise(prep.df_comp)

    # Random Walk
    wlk = RandomWalk()

    # Stationarity
    Stationarity(wnoise.df_comp, wlk.walk)

    # ACF #PCF
    AcfAndPcf(wnoise.df_comp)

    # AutoRegressor
    Autoregressor(wnoise.df_comp)

    # Rolling window
    RollingWindow(wnoise.df_comp)


run()

