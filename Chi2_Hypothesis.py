from scipy.stats import chi2_contingency
data=[[141,68,4],[179,159,7],[220,216,4],[86,101,4]]
stat,p,dof,expected=chi2_contingency(data)
alpha=0.05
print("P Value is:",p)
if p<=alpha:
    print("Yes! There is relationship between age group and their movie genre inclination")
else:
    print("No! There is no relationship between age group and their movie genre inclination")