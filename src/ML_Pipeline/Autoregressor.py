from statsmodels.tsa.arima_model import ARMA
from scipy.stats.distributions import chi2

#create a class for autoregressor model
class Autoregressor:

    def __init__(self, df_comp):
        self.df_comp = df_comp
        
        # AR 1
        model_ar = self.AR_model(1)
        model_ar_2 = self.AR_model(2)

        print(self.LLR_test(model_ar, model_ar_2))

    def AR_model(self, order):
        # AR
        model_ar_2 = ARMA(self.df_comp.IoT_Reading, order=(order, 0))
        results_ar_2 = model_ar_2.fit()
        results_ar_2.summary()
        return model_ar_2

    def LLR_test(self, model_1, model_2, DF=1):
        L1 = model_1.fit().llf
        L2 = model_2.fit().llf
        LR = (2 * (L2 - L1))
        p = chi2.sf(LR, DF).round(3)
        return p
