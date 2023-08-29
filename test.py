import pandas as pd

pd.set_option("display.max_columns", None)
df = pd.read_csv("price_paid_records.csv")

## Sample Generator
# df_s = df.sample(n=100000, random_state=108)
# df_s.to_csv('price_samples.csv')

## Extraction
# county = "CLWYD"
# county_df = df[df['County'] == county]
# print(county_df)