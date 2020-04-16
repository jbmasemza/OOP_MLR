import numpy as np

class ErrorCalculator:

    def __init__(self, y, y_pred):

        self.y          =   np.array(y)       
        self.y_pred     =   np.array(y_pred)  

   

    def dimention(self):

        if len(self.y.shape) == len(self.y_pred.shape):
            return True

        else:
            raise ValueError(f'shape of y: {self.y} != shape of y_pred: {self.y_pred}')



    def get_residuals(self):

        residuals = self.y - self.y_pred
        return residuals

    def get_standardised_residuals(self):

        standardised_residuals = self.get_residuals() / (self.get_residuals()/std())
        return standardised_residuals

    def get_mse(self):

        mse = np.square(np.subtract(self.y , self.pred)).mean()
        return mse

    def get_rmse(self):

        rmse = np.sqrt(((self.y_pred - self.y)**2).mean())
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
        print(f'max rmse: {rmse_max}')
        print(f'min mse: {mse_min}')
        print(f'max mse: {mse_max}')
