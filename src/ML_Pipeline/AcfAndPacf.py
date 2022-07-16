import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt

# create a class for ACF and PACF
class AcfAndPcf:

    def __init__(self, df_comp):
        # ACF
        self.acf_plot(df_comp)

        # PACF
        self.pcf_plot(df_comp)


    def pcf_plot(self, df_comp):
        """
        PCF plotting
        :return:
        """
        sgt.plot_pacf(df_comp.IoT_Reading, lags=40, zero=False, method=("ols"))
        plt.title("PACF IoT Reading")
        plt.savefig("../output/"+"PACF.png")
        sgt.plot_pacf(df_comp.wn, lags=40, zero=False, method=("ols"))
        plt.title("PACF White Noise")
        plt.savefig("../output/"+"PACF-WN.png")

    def acf_plot(self, df_comp):
        """
        ACF plotting
        :return:
        """
        sgt.plot_acf(df_comp.IoT_Reading, lags=40, zero=False)
        plt.title("ACF IoT Reading")
        plt.savefig("../output/"+"ACF.png")
        sgt.plot_acf(df_comp.wn, lags=40, zero=False)
        plt.title("ACF White Noise")
        plt.savefig("../output/"+"ACF-WN.png")
