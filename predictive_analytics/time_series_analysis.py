import numpy as np
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

def arima_forecast(data, order=(5,1,0)):
    model = ARIMA(data, order=order)
    model_fit = model.fit(disp=0)
    return model_fit.forecast()[0]
