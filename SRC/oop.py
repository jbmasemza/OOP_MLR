
from sklearn.metrics import mean_squared_error as mse
import matplotlib.pyplot as plt
import numpy as np


# ErrorCalculator Class
class ErrorCalculator:

    def __init__(self, y, y_predict):

        self.y          =   np.array(y)       
        self.y_predict     =   np.array(y_predict)  


    def get_residuals(self):

        residuals = self.y - self.y_predict
        return residuals

    def get_standardised_residuals(self):

        standardised_residuals = self.get_residuals() / (self.get_residuals()/std())
        return standardised_residuals

    def get_mse(self):

        mse = np.square(np.subtract(self.y, self.y_predict)).mean()
        return mse

    def get_rmse(self):

        rmse = np.sqrt(((self.y_predict - self.y)**2).mean())
        return rmse

    def error_summary(self):
        std_resid_min = min(self.std_res)
        std_resid_max = max(self.std_res)
        rmse_min = min(self.rmse)
        rmse_max = max(self.rmse)
        mse_min = min(self.mse)
        mse_max = max(self.mse)
        print(f'standard residual: {std_resid_min}')
        print(f'standard residual: {std_resid_max}')
        print(f'min rmse: {rmse_min}')


# Plotter
class Plotter():
    def __init__(self,y_test,ypred):
        self.y_test = y_test
        self.ypred = ypred
    
    def run_calculations(self):
        return self.y_test - self.ypred
    
    def plot(self):
        plt.hist(self.y_test - self.ypred)
        plt.title('Residuals Plot for predictions')
        plt.xlabel('Residuals')
        plt.ylabel('Frequency')
        return plt.show()

# Class histogram plotter
class HistogramPlotter(Plotter):
    def __init__(self, y_test,ypred):
        Plotter.__init__(self, y_test, ypred)

#Class scatter plotter        
class ScatterPlotter(Plotter):
    def __init__(self, y_test, ypred):
        Plotter.__init__(self, y_test, ypred)

    def plot(self):
        chart = pd.DataFrame({"y_test": self.y_test, "y_prediction": self.ypred})
        chart.plot.scatter(x="y_test", y="y_prediction", c="DarkBlue")
        plt.title("Prediction vs Actual values")
        plt.xlabel("Actual")
        plt.ylabel("Prediction")
        return plt.show()