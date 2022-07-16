import pandas as pd
import seaborn as sns
sns.set()

from MLPipeline.WhiteNoise import WhiteNoise
from MLPipeline.Preprocess import Preprocess
from MLPipeline.AcfAndPacf import AcfAndPcf
from MLPipeline.Autoregressor import Autoregressor
from MLPipeline.RandomWalk import RandomWalk
from MLPipeline.RollingWindow import RollingWindow
from MLPipeline.Stationarity import Stationarity

def run():
    # importing the data
    raw_csv_data = pd.read_csv("input/Data-Chillers.csv")

    df_comp = raw_csv_data.copy()

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

