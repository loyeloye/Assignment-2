import pandas as pd
from pandas import Series, DataFrame

# example - Revenue of companies
revenue_df = pd.read_clipboard(sep='    ')
print(revenue_df)

#index and columns
print (revenue_df.columns)

print(revenue_df['Rank'])