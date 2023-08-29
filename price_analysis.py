import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# As the records were too much to process with my laptop, I have taken a smaller size sample which would be much more reasonable to deal with

# A function which takes in a given set of coordinate points and plots them
def plot(xpoints, ypoints, a, b, county):
    plt.title(county)
    plt.xlabel("Year")
    plt.ylabel("Mean House Price")
    plt.scatter(xpoints, ypoints, color='purple')
    plt.plot(xpoints, a * xpoints + b)
    plt.show()


pd.set_option("display.max_columns", None)
raw_df = pd.DataFrame(pd.read_csv('price_paid_records.csv'))

# Cleaning the data so that only data which is necessary is processed
# This also involves converting the Date from a String form to an Integer form
df = raw_df[["Price", "Date of Transfer", "County", "Property Type"]]
df["Date of Transfer"] = df["Date of Transfer"].str[:4]
df['Date of Transfer'] = df['Date of Transfer'].astype(int)
df = df.sort_values(["County", "Date of Transfer"])

county_list = set()
for county in df['County']:
    county_list.add(county)

# Analysing the increase in house prices using the data
gradients = {}
ranges = {}
property_types_count = {}
for county in county_list:
    years = []
    year_means = []
    f = t = d = s = 0
    county_df = df[df['County'] == county]
    for year in range(1995, 2018):
        # Calculating means for each individual county
        year_mean = county_df[county_df['Date of Transfer'] == year]
        year_mean = year_mean['Price'].mean()

        year_means.append(year_mean)
        years.append(year)

    f = len(county_df[county_df['Property Type'] == "F"])
    s = len(county_df[county_df['Property Type'] == "S"])
    d = len(county_df[county_df['Property Type'] == "D"])
    t = len(county_df[county_df['Property Type'] == "T"])
    property_types_count[county] = {"F": f, "D": d, "S": s, "T": t}
    # I print the data needed for any county after the main code is run

    xpoints = np.array(years)
    ypoints = np.array(year_means)

    # Approximating a linear regression line
    a, b = np.polyfit(xpoints, ypoints, 1)
    gradients[county] = a
    ranges[county] = max(year_means) - min(year_means)

    county_to_search = "Greater London".upper()
    if county == county_to_search:
        print(a)
        plot(xpoints, ypoints, a, b, county)

sorted_gradients = dict(sorted(gradients.items(), key=lambda x: x[1], reverse=True))
sorted_ranges = dict(sorted(ranges.items(), key=lambda x: x[1], reverse=True))

# Prints the property count for the specified county
print(property_types_count["BLACKPOOL"])

# Required Outputs
print(sorted_gradients)
print(sorted_ranges)

## Calculates the total of housing within each county (w/o considering year)
df = raw_df[["Price", "County"]]
county_means = df.groupby(['County']).mean()
county_means = county_means.sort_values(by=['Price'])
print("Top 5 most expensive counties to live in:")
print(county_means.tail())

print("Top 5 most cheap counties to live in: ")
print(county_means.head())
