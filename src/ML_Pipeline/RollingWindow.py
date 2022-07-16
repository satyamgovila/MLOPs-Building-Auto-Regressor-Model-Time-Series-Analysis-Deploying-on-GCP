
# create a class for rolling and expanding window
class RollingWindow:
    
    def __init__(self, df_comp):
        self.df_comp = df_comp
        # Rolling Window
        self.rollingWindow()

        # Expanding Window
        self.expandingWindow()

    def expandingWindow(self):
        """
        Expanding Window
        :return:
        """
        self.df_comp['rolling_mean_IoT_Reading'] = self.df_comp['IoT_Reading'].expanding(min_periods=1).mean()
        print(self.df_comp.rolling_mean_IoT_Reading)
        self.df_comp['rolling_mean_IoT_Reading'] = self.df_comp['IoT_Reading'].expanding(min_periods=1).std()
        print(self.df_comp.rolling_mean_IoT_Reading)

    def rollingWindow(self):
        """
        Rolling Window
        :return:
        """
        self.df_comp['rolling_mean_IoT_Reading'] = self.df_comp['IoT_Reading'].rolling(
            window=24).mean()  # Window size is 24 here
        self.df_comp.tail()
        self.df_comp['rolling_mean_IoT_Reading'] = self.df_comp['IoT_Reading'].rolling(
            window=24).std()  # Window size is 24 here
        self.df_comp.tail()