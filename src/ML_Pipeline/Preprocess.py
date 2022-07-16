import scipy.stats
import pylab
import matplotlib.pyplot as plt
import pandas as pd


# create a class for preprocessing the data
class Preprocess:
    
    def __init__(self, df_comp):

        self.df_comp = df_comp

        # Plotting the data as line plots
        self.plot_data()

        # Plotting the data as QQ plots
        self.plot_QQPlots()

        # Changing date to datetime format
        self.set_date_index()

        # Setting the frequency
        self.set_freq()

        #Filling Missing Values
        self.fill_missing_values()

        # Reshape univariate data
        self.reshape_data()

    def reshape_data(self):
        """
        Reshape univariate data
        :return:
        """
        self.df_comp["IoT_Reading"] = self.df_comp.IOT_Sensor_Reading
        self.df_comp.describe()
        del self.df_comp['IOT_Sensor_Reading']
        del self.df_comp['Error_Present']
        del self.df_comp['Sensor_2']
        del self.df_comp['Sensor_Value']

    def fill_missing_values(self):
        """
        Filling Missing Values
        :return:
        """
        self.df_comp.IOT_Sensor_Reading = self.df_comp.IOT_Sensor_Reading.fillna(method="ffill")
        self.df_comp.Error_Present = self.df_comp.Error_Present.fillna(method="bfill")
        self.df_comp.Sensor_2 = self.df_comp.Sensor_2.fillna(method="bfill")
        self.df_comp.Sensor_Value = self.df_comp.Sensor_Value.fillna(value=self.df_comp.Sensor_Value.mean())

    def set_freq(self):
        """
        Setting the frequency
        :return:
        """
        self.df_comp = self.df_comp.asfreq('H')

    def set_date_index(self):
        """
        Changing date to datetime format
        :return:
        """
        # taken as text field
        self.df_comp.time = pd.to_datetime(self.df_comp.time, format='%d-%m-%Y %H:%M')
        self.df_comp.set_index("time", inplace=True)

    def plot_QQPlots(self):
        """
        Plotting the data as QQ plots
        :return:
        """
        # The QQ plot
        scipy.stats.probplot(self.df_comp.IOT_Sensor_Reading, plot=pylab)
        plt.title("QQ plot for IOT_Sensor_Reading")
        pylab.savefig("../output/"+"QQ_IOT_Sensor.png")
        # The QQ plot
        scipy.stats.probplot(self.df_comp.Error_Present, plot=pylab)
        plt.title("QQ plot for Error_Present")
        pylab.savefig("../output/"+"QQ_Error_Present.png")
        # The QQ plot
        scipy.stats.probplot(self.df_comp.Sensor_2, plot=pylab)
        plt.title("QQ plot for Sensor_2")
        pylab.savefig("../output/"+"QQ_Sensor_2.png")
        # The QQ plot
        scipy.stats.probplot(self.df_comp.Sensor_Value, plot=pylab)
        plt.title("QQ plot for Sensor_Value")
        pylab.savefig("../output/"+"QQ_Sensor_Value.png")

    def plot_data(self):
        """
        Plotting the data as line plots
        :return:
        """
        self.df_comp.IOT_Sensor_Reading.plot(figsize=(20, 5), title="IOT Sensor_Reading")
        plt.savefig("../output/"+"IOT_Sensor.png")
        self.df_comp.Error_Present.plot(figsize=(20, 5), title="Error_Present")
        plt.savefig("../output/"+"Error_Sensor.png")
        self.df_comp.Sensor_2.plot(figsize=(20, 5), title="Sensor_2")
        plt.savefig("../output/"+"Sensor_2.png")
        self.df_comp.Sensor_Value.plot(figsize=(20, 5), title="Sensor_Value")
        plt.savefig("../output/"+"Sensor_Value.png")
