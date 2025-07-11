import pandas as pd
# remember to install statsmodels before running this script
# you can do it with pip install statsmodels
#and also numpy
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
from linearmodels import PanelOLS 



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

# de-mean the data
mean_by_id = data_fe.groupby('iid').transform('mean', numeric_only=True)
print(mean_by_id)
print(data_fe)

y_demeaned= data_fe['outcome'] - mean_by_id['outcome']
D_demeaned = data_fe['D'] - mean_by_id['D']
result_fe = sm.OLS(y_demeaned, sm.add_constant(D_demeaned)).fit(cov_type='cluster',
    cov_kwds={'groups': data_fe['iid']})
print(result_fe.summary())
