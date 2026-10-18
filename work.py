import pandas as pd
import numpy as np
df = pd.read_excel('C:/Users/geeta/Downloads/data.csv.xlsx')
df.info()
null = df.isnull().sum()
print("NULL values :",null)
statistics = df.describe()
print("STATISTICS values :",statistics)

# Fill missing values
df["Duration"] = df["Duration"].fillna(0)
df["Calories"] = df["Calories"].fillna(0)

#handling duplicates
dulp = df.duplicated().sum()
print(" total duplicated values :",dulp)
remove_dulps = df.drop_duplicates(inplace=True)
print(" remove duplicate values :",remove_dulps)

#invalid values
df.loc[df["Duration"] > 100, "Duration"] = np.nan

#filtered rows
filtered_df = df[df["Calories"] < 200]
print(filtered_df)

#outlier
print(df["Duration"].describe())
print(df["Duration"].sort_values())

#create new column
df["Exercise"] =df["Duration"] + df["Calories"]
print(df[["Duration","Calories","Exercise"]])
