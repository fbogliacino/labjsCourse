#remember to install pandas before running this script
#you can do it with pip install pandas
# import pandas as pd
import pandas as pd
# remember to install scipy before running this script
# you can do it with pip install scipy
from scipy import stats
# remember to install openpyxl before running this script
# you can do it with pip install openpyxl
excel_data_df = pd.read_excel('Esercizi-in-classe-full-data (1).xlsx', sheet_name='data')
print(excel_data_df.head())  # Display the first few rows of the DataFram
excel_data_df['date'] = excel_data_df['timestamp'].astype(str).str[:4]
print(excel_data_df['date'].head())  # Display the first few rows of the DataFrame with the new 'date' column
selected_data=excel_data_df.loc[(excel_data_df['date'] <= '2024')&(excel_data_df['sender']=='Main Question')]
print(selected_data.shape) # Prints (number_of_rows, number_of_columns) 
print(selected_data.info()) # Display the DataFrame information 

cols_to_drop = selected_data.columns[42:63]  # 66 because the stop index is exclusive
selected_data = selected_data.drop(columns=cols_to_drop)
selected_data['treatment'].loc[(selected_data['treatment'].isna()) & (selected_data['Index']<=74)] =  'BAS'
selected_data['treatment'].loc[(selected_data['treatment'].isna()) & (selected_data['Index']>74)] =  'P1E'
print(selected_data.info()) # Display the DataFrame information
print(selected_data) 

# Perform a chi-square test of independence
# Create a contingency table
contingency_table = pd.crosstab(selected_data['eleccion5'], selected_data['treatment'])

# Run the chi-square test of independence
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

print("Chi2:", chi2)
print("p-value:", p)


# perform a Wilcoxon signed-rank test
eleccionTest = stats.wilcoxon(selected_data['eleccion5'], selected_data['eleccion0'], alternative='two-sided', method='asymptotic')
print(eleccionTest)
