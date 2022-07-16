import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

#create a function for whitenoise
class WhiteNoise:

    def __init__(self, df_comp):

        self.df_comp = df_comp

        # Generate Random Whitenoise data
        self.generate_whitenoise()

        # plot comparison data
        self.plot_data_comparison()

        # plot autocorrelation
        self.autocorrelation_plot()

    def autocorrelation_plot(self):
        """
        plot autocorrelation plots
        :return:
        """
        autocorrelation_plot(self.df_comp.IoT_Reading)
        plt.savefig("../output/"+"autocorrelationIoT.png")
        # Plot shows +ve correlation with lag values but here no significant relationship is seen with lag values. No Cycles/Trends
        autocorrelation_plot(self.df_comp.wn)
        plt.savefig("../output/"+"WN.png")

    def plot_data_comparison(self):
        """
        plot comparison data
        :return:
        """
        self.df_comp.wn.plot(figsize=(20, 5))
        plt.title("White noise time-series", size=24)
        plt.savefig("../output/"+"whitenoise.png")
        self.df_comp.IoT_Reading.plot(figsize=(20, 5))
        plt.title("IoT_Reading Series", size=24)
        plt.savefig("../output/"+"IOT_Reading.png")
        self.df_comp.wn.plot(figsize=(20, 5))
        self.df_comp.IoT_Reading.plot(figsize=(20, 5))
        plt.title("White nosie vs IoT_Reading Series", size=24)
        plt.savefig("../output/"+"compWNvsIOT.png")

    def generate_whitenoise(self):
        """
        Generate Random Whitenoise data
        :return:
        """
        wn = np.random.normal(loc=self.df_comp.IoT_Reading.mean(), scale=self.df_comp.IoT_Reading.std(),
                              size=len(self.df_comp))
        self.df_comp["wn"] = wn
