#Reepo to calculate most commmon adamsndler choices

import pandas as pd 

sandler = r"C:\Users\Matth\Downloads\Adam sandler movies  (Responses).xlsx"

#Im not that special at it, im just autsitc


df = pd.read_excel(sandler)
    

#Rank all the counts:
    
df['Rank'] = df['Top 5 Adam Sandler movies?'].rank(method='min', ascending=False)


import pandas as pd



df['Counts'] = df["Top 5 Adam Sandler movies?"]

import pandas as pd


# Split the counts and convert to numeric
df['Counts'] = df['Counts'].apply(lambda x: [str(i) for i in x.split(',')])

# Explode the counts to individual rows
exploded_df = df.explode('Counts')

# Sum the counts
exploded_df['Sum_Counts'] = exploded_df.groupby('Counts')['Rank'].transform('sum')

# Count unique values
unique_counts = exploded_df['Counts'].value_counts().reset_index()
unique_counts.columns = ['Value', 'Count']

# Rank the counts
unique_counts['Rank'] = unique_counts['Count'].rank(method='min', ascending=False)

# Merge back to exploded DataFrame
result = exploded_df.merge(unique_counts, how='left', left_on='Counts', right_on='Value')

# Drop the 'Value' column as it is redundant now
result.drop(columns=['Value'], inplace=True)

print(result)
