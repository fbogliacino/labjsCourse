#remember to install pandas before running this script
#you can do it with pip install pandas
# import pandas as pd
import pandas as pd
# remember to install scipy before running this script
# you can do it with pip install scipy
from scipy import stats
# remember to install openpyxl before running this script
# you can do it with pip install openpyxl
data = pd.read_excel('SimulatedData.xlsx', sheet_name='database')
print(data.head())

# Perform a chi-square test of independence
# Create a contingency table
contingency_table = pd.crosstab(data['outcome1'], data['treatment'])

# Run the chi-square test of independence
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

print("Chi2:", chi2)
print("p-value:", p)

# run a kolmogorov-smirnov test
# for the two groups in the treatment column
# using the amountSent (DG) as outcome variable

