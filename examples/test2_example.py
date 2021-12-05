import pandas as pd
from ck_wrapper import CorrelationKit

# set a dataframe or read from a csv file
d = {'x': ['large', 'large', 'small', 'small'], 'y': ['hot', 'hot', 'cold', 'cold'],'z':[0,1,2.5,3]}
df = pd.DataFrame(data=d)

# set x label and y label for correlation, which is suitable for binary variables
r_p,r_s,r_k=CorrelationKit(df).get_corr_between_category_and_continual('x','large','z') # large=1; otherewise 0

# results
print('pearson: ',r_p)
print('speraman: ',r_s)
print('kendalltau: ',r_k)
