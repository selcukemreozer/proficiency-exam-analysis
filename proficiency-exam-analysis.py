# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 23:45:38 2023

@author: selcu
"""
#%% file settings
# import tabula
import pandas as pd

# tabula.convert_into("jan_2023_proficiency.pdf", "jan_2023_proficiency.csv", output_format = "csv", pages = 'all')
df = pd.read_csv("jan_2023_proficiency.csv", encoding='latin1')

#%% cleaning data
listC = list(df[df['Number'] == 'Number'].index) # indexing trash rows
df.drop(labels=listC, axis = 0, inplace=True) # deleting trash rows

df.drop(['Number', 'Name', 'Surname'], axis = 1, inplace=True) # deleting trash columns

for each in df.columns:
    df[each] = [float(e.replace(',','.')) for e in df[each]] # converting from string to float type of values

#%% calculating
winners = df[(df['Session 1'] >= 25) & (df['Session 2'] >= 25) & (df['Total'] >= 60)]
condition2 = df[(df['Session 1'] < 25) & (df['Session 2'] >= 25) & (df['Total'] >= 60)]
condition3 = df[(df['Session 1'] >= 25) & (df['Session 2'] < 25) & (df['Total'] >= 60)]
"""
condition1(passers):
    Session 1 >= 25
    Session 2 >= 25
    Total >= 60
    
condition2(participants who didn't pass because of session1):
    Session 1 < 25
    Session 2 >= 25
    Total >= 60
    
condition3(participants who didn't pass because of session2):
    Session 1 >= 25
    Session 2 < 25
    Total >= 60
"""
THEnumber_of_passers = len(winners)
win_percent = round((len(winners)*100)/len(df))

listOfAverages = list()
listOfMaxes = list()
for each in df.columns: # the max value and the mean value of sessions
    listOfAverages.append(round(df[each].mean(), 2))
    listOfMaxes.append(int(df[each].max()))
    
#%% printing results

print(f"The number of Passers:{THEnumber_of_passers}(%{win_percent})")
print(f"The number of participant who didn't pass because of session1 :{len(condition2)}")
print(f"the number of participant who didn't pass because of session2 :{len(condition3)}")

for each in range(len(df.columns)):
    print(f"\nThe max of {df.columns[each]} :{listOfMaxes[each]}")
    print(f"The average of {df.columns[each]} :{listOfAverages[each]}\n")
    
    
    
    
    
    