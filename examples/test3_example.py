import pandas as pd
from ck_wrapper import CorrelationKit

# set a dataframe or read from a csv file
d = {'x': ['large', 'large', 'middle','small', 'small'], 'y': ['hot', 'hot','warm', 'cold', 'cold'],'z':[0,1,2,2.5,3]}
df = pd.DataFrame(data=d)

# set x label and y label for correlation, which is suitable for multiple-category variables
F,p=CorrelationKit(df).get_f_oneway('x',['large','middle','small'],'z')

# results
print('F: ',F)
print('p: ',p)

