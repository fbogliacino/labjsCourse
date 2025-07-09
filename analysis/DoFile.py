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
print(data.info())
# Perform a chi-square test of independence
# Create a contingency table
contingency_table = pd.crosstab(data['outcome1'], data['treatment'])

# Run the chi-square test of independence
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

print("Chi2:", chi2)
print("p-value:", p)

#run the Fisher's exact test
fisher_result = stats.fisher_exact(contingency_table)
print("Fisher's Exact Test result:", fisher_result)

# run a kolmogorov-smirnov test
# for the two groups in the treatment column
# using the amountSent (DG) as outcome variable
sample1=data.amountSent[data.treatment ==1]
#print(sample1)
sample2=data.amountSent[data.treatment ==0]
#print(sample2)
ks_analysis = stats.ks_2samp(sample1, sample2)
print('pvalue', ks_analysis.pvalue)

# run a Mann-Whitney U test
mannwhitney_result = stats.mannwhitneyu(sample1, sample2, alternative='two-sided')
print("Mann-Whitney U test result:", mannwhitney_result)

# run an epps Singleton test    
epps_singleton_result = stats.epps_singleton_2samp(sample1, sample2)
print("Epps-Singleton test result:", epps_singleton_result)

# run  a Kruskal Wallis test for multiple groups
group1 = data.outcome2[data.conditions==0]
group2 = data.outcome2[data.conditions==1]
group3 = data.outcome2[data.conditions==2]
group4 = data.outcome2[data.conditions==3]
kruskal_result = stats.kruskal(group1, group2, group3, group4)
print("Kruskal-Wallis test result:", kruskal_result)