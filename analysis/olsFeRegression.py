import pandas as pd
# remember to install statsmodels before running this script
# you can do it with pip install statsmodels
#and also numpy
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
# Load the data
data = pd.read_excel('SimulatedData.xlsx', sheet_name='database')
print(data.head())
D=data.treatment
Y=data.outcome1
# Fit the OLS regression model
result = sm.OLS(Y, sm.add_constant(D)).fit()
print(result.summary())