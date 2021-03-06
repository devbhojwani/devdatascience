# -*- coding: utf-8 -*-
"""VizPractice_Countdown2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zFk6GeBVhyMWTFwy2oVh5_rPbt-WCmvo
"""

# import packages
import matplotlib.pyplot as plt  # for viz
import seaborn as sns  # for viz
import pandas as pd  # for data manipulation and analysis
import numpy as np  # math funcitonality

"""# We're going to be looking at data about passwords!
https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-01-14
"""

# import data
data = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-14/passwords.csv')
data.head()

# drop rows with NaN values (we will go over later better ways to handle this)
data.dropna(inplace=True)

# create a password character length column
data['length'] = data['password'].apply(len)
data.head()
print('hi')

"""# Continuous analysis"""

# examine relationship between popularity (rank) and time to crack (offline_crack_sec)
sns.relplot(x = 'rank', y = 'offline_crack_sec', kind = 'scatter', hue="time_unit", data = data)
plt.title('Popularity vs Crack Time')
plt.xlabel("Rank")
plt.ylabel("Time to Crack")
plt.show()

# examine relationship between popularity (rank) and strength
rank = data["rank"]
strength = data["strength"]
plt.scatter(rank,strength)
plt.xlabel("Rank")
plt.ylabel("Password Strength")
plt.title("Password Popularity versus Password Strength")
plt.show()

sns.lmplot(x='rank', y='strength', data=data)
plt.show()

# examine relationship between popularity (rank) and strength and length
sns.relplot(x='rank', y='strength', hue='length', data=data, color='blue')
plt.title('Popularity vs strength and length')
plt.show()

sns.catplot(x='strength', y='rank', data=data, kind='swarm', hue='length')
plt.title('Popularity vs Strength of Passwords')
plt.xticks(rotation=90)
plt.show()

"""# Categorical analysis"""

# examine distribution of number of password in each time_unit
sns.catplot(x = 'time_unit', kind = 'count', data = data)
plt.title("Distribution of Number of Passwords by Time Unit")
plt.show()

sns.catplot(x='time_unit', kind='count', data=data, order=['seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years'])
plt.title('Number of passwords per time it took to crack them')
plt.show()

# examine relationship between category and strength
category = data['category']
sns.catplot(x = 'category', y = 'strength', kind = 'boxen', 
            data = data)
plt.xticks(rotation = 90)
plt.show()

# examine relationship between category and length
sns.catplot(x='category', y='length', data=data, kind='violin')
plt.xticks(rotation = 90)
plt.title("Category of Password v. Length")
plt.ylabel("Length")
plt.xlabel("Category")
plt.show()

"""# Make your own visualization about something you'd like to explore in this dataset!"""

