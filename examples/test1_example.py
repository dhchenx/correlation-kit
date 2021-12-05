import pandas as pd
from ck_wrapper import CorrelationKit

# set a dataframe or read from a csv file
d = {'x': [1, 2, 3.5, 4], 'y': [3, 4, 4.5, 6]}
df = pd.DataFrame(data=d)

# set x label and y label for correlation
x = "x"
y = "y"

# calc
def get_correlation(x, y, corr_type):
    stat = 0
    p = 0
    if corr_type == "pearson":
        stat, p = CorrelationKit(df).get_pearson(x, y)
    elif corr_type == "spearman":
        stat, p = CorrelationKit(df).get_spearman(x, y)
    elif corr_type == "kendalltau":
        stat, p = CorrelationKit(df).get_kendalltau(x, y)
    return stat, p


# print results
print("pearson = ", get_correlation(x, y, "pearson"))
print("spearman = ", get_correlation(x, y, "spearman"))
print("kendalltau = ", get_correlation(x, y, "kendalltau"))
