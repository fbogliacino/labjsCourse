import pandas as pd
# remember to install statsmodels before running this script
# you can do it with pip install statsmodels
#and also numpy
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
from linearmodels import PanelOLS 
from fixedeffect import fixedeffect



# Load the data
data = pd.read_excel('SimulatedData.xlsx', sheet_name='database')
print(data.head())
D=data.treatment
Y=data.outcome1
# Fit the OLS regression model
result = sm.OLS(Y, sm.add_constant(D)).fit()
print(result.summary())

# Save the results to a text file
with open('ols_results.txt', 'w') as f:
    f.write(result.summary().as_text()) 

#now import the new data to estimate with Fixed Effects    
data_fe = pd.read_excel('panelData.xlsx', sheet_name='panel')
print(data_fe.head())

# Fit the Fixed Effects regression model