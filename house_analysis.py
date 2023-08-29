import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
import re

houses_df = pd.read_csv('Average_UK_houseprices_and_salary.csv')
income_df = pd.read_csv('Income_by_age_and_gender.csv')

houses_df.drop('Unnamed: 3', axis=1, inplace=True)

houses_df.columns = [x.rsplit(' ', 4)[0] for x in houses_df.columns]
houses_df.columns = [re.sub(r'\s+', '_', x).lower() for x in houses_df.columns]

plt.figure(figsize=(25, 9))
sns.regplot(data=houses_df, x='year', y='average_house_price', scatter_kws={"s": 100}, ci=15)
plt.title('UK Average House Prices (1975-2020)')
plt.xlabel('Year')
plt.ylabel('Average house price adj. by inflation (pounds)')
plt.show()

slope, intercept = np.polyfit(houses_df.year, houses_df.average_house_price, 1)

print('Average house price adj. by inflation have gone up by: £' + str(round(slope, 2)))

plt.figure(figsize=(25, 9))
sns.regplot(data=houses_df, x='year', y='median_salary', scatter_kws={"s": 100}, ci=15)
plt.title('UK Median Salary (1975-2020)')
plt.xlabel('Year')
plt.ylabel('Median Salary adj. by inflation (pounds)')
plt.show()

slope, intercept = np.polyfit(houses_df.year, houses_df.median_salary, 1)
print('Median Salary adj. by inflation have gone down by: £' + str(round(slope, 2)))

print(income_df.describe())

plt.figure(figsize=(25,9))
sns.barplot(data=income_df, x='Median salary (pounds)', y='Age group', hue='Gender')
plt.title('UK Median Salary (1975-2020)')
plt.xlabel('Median Salary adj. by inflation (pounds)')
plt.ylabel('Age Group')
plt.show()
