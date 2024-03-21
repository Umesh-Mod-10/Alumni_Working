# %% Importing the necessary libraries:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import re

# %%

'''
# Finding the duplicates, incomplete and unregistered when compared to the current data sheet
# And mark them in the current data sheet only by adding additional columns.
# NO changes must be made to the All ALumni Details sheet.
'''

# %% Importing the dataset:

data = pd.read_csv(r"C:\Users\umesh\OneDrive\Desktop\Alumini Dataset.csv")
df = pd.read_excel(r"C:\Users\umesh\OneDrive\Desktop\NEC Alumni Association Chennai Chapter Member’s Data (Responses).xlsx")

# %% Getting the basic details:

print(data.info())
print(data.duplicated().sum())
print(data.isna().sum()[data.isna().sum() != 0])

# %% Calculating the null value percentage:

null = data.isna().sum()[data.isna().sum() != 0]
cond_null = (((null/data.shape[0])*100).sort_values(ascending=False))
print(cond_null)

# %% Getting the blank values to be Nan:

data.replace(to_replace='^\s{1,}', regex=True, inplace=True, value=np.nan)

# %% Getting out the Unwanted columns:

data.drop(columns=(cond_null[cond_null > 92].index), inplace=True, axis=1)

# %% Checking the Nan percentage:

null = data.isna().sum()[data.isna().sum() != 0]
cond_null = (((null/data.shape[0])*100).sort_values(ascending=False))
print(cond_null)

# %% Getting the column to find Nan values:

data['Status'] = 'Orginal'

# %% Removing the dots from name:

data['Name'] = data['Name'].apply(lambda x: x.replace(".", ""))

# %% Getting the duplicates on the first round:

dup = data.loc[data.duplicated(keep=False)]
print(data.duplicated().sum())
dup_l = data[data.duplicated()]
#name = dup_l['Name'].values
#data['Status'] = data['Status'].apply(lambda x: 'Duplicate' if data['Name'] is in )

# %% Handling the Gender Nan values:

gender_nan = (data[data['Gender'].isna() & data['Salutation'].notna()])

Male = data[(data['Salutation'] == 'Mr. ') & data['Gender'].isna()]
Female = data[(data['Salutation'] == 'Ms. ') & data['Gender'].isna()]

data.loc[Male.index,'Gender'] = data.loc[Male.index,'Gender'].fillna('M')
data.loc[Female.index,'Gender'] = data.loc[Female.index,'Gender'].fillna('F')

# %%

df = df[['Name', 'Batch', 'Work Details and Organisation', 'Residence']]
print(df.info())
print(df.duplicated().sum())
print(df.isna().sum()[df.isna().sum() != 0])

# %%

df_one = df[['Name', 'Batch']]
print(df_one.duplicated().sum())
print(df_one[df_one.duplicated()])
print(df[(df_one['Name'] == 'Suresh') & (df_one['Batch']==1998.0)])