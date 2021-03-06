# -*- coding: utf-8 -*-
"""recomm_knn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D1CD0ySDY0X1nJAYAEmHd1p6aDSu94tc

#EDA
"""

!git clone https://github.com/conwayyao/Recipe-Analysis

import pandas as pd
recipe_data = pd.read_csv('/content/Recipe-Analysis/CuisineAnalyzer/cuisinedata/indian.csv')

recipe_data = recipe_data.drop(['id', 'rating', 'totalTimeInSeconds'], axis = 1)

len(recipe_data)

recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Mango Lassi'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Indian Butter Chicken'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Tandoori Chicken'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Easy Chicken Tikka Masala'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Cucumber Raita'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Healthy Paneer Makhani'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Indian Mini Garlic Naan'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Grilled Tandoori Chicken'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Slow-Cooker Coconut Chicken Tikka Masala'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Chicken Tikka Masala'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Aloo Palak (Indian Potatoes & Spinach)'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'West Indian Lamb Curry'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Shami Kabab'].index[1:], axis = 0)
recipe_data = recipe_data.drop(recipe_data.loc[recipe_data['recipeName'] == 'Coconut Chutney'].index[1:], axis = 0)

import numpy as np
recipe_data.insert(loc = 0, column = 'id', value = np.arange(len(recipe_data)))

recipe_data.info()

recipe_data = recipe_data.rename(columns={'id':'recipe_id'})

user_data = pd.DataFrame(columns = ['user_id', 'recipe_id', 'ratings'])

user_data = user_data[0:0]

for i in range(1, 101):
  r = np.random.choice(np.arange(1, 6), p=[0.01, 0.04, 0.20, 0.35, 0.4], size = len(recipe_data))
  for i1 in range(len(recipe_data)):
    user_data = user_data.append({'user_id':i, 'recipe_id': i1, 'ratings':r[i1]}, ignore_index=True)

recipe_data.to_csv('recipe_data.csv')

user_data.to_csv('user_data.csv')

recipe_data = pd.read_csv('/content/recipe_data.csv')
user_data = pd.read_csv('/content/user_data.csv')

recipe_data = recipe_data.drop(recipe_data.columns[0], axis = 1)
user_data = user_data.drop(user_data.columns[0], axis = 1)

user_data_merge = pd.merge(user_data, recipe_data, on = 'recipe_id')

user_data_merge = user_data_merge.drop(['course',	'cuisine',	'ingredients'], axis = 1)

user_data_merge = user_data_merge.drop(user_data_merge.sample(frac = 0.25).index, axis = 0)

user_data_merge

recipe_ratingCount = (user_data_merge.groupby(by = ['recipeName'])['ratings'].count().reset_index().rename(columns = {'ratings': 'totalRatingCount'})[['recipeName', 'totalRatingCount']])
recipe_ratingCount.sort_values('totalRatingCount', ascending = False).head(20)

rating_with_totalRatingCount = user_data_merge.merge(recipe_ratingCount, left_on = 'recipeName', right_on = 'recipeName', how = 'left')
rating_with_totalRatingCount.head()

popularity_threshold = 70
rating_popular_recipe= rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')
rating_popular_recipe

rating_popular_recipe.shape

recipe_features_df=user_data_merge.pivot_table(index='recipeName',columns='user_id',values='ratings').fillna(0)
recipe_features_df

from scipy.sparse import csr_matrix

recipe_features_df_matrix = csr_matrix(recipe_features_df.values)

from sklearn.neighbors import NearestNeighbors

model_knn = NearestNeighbors(n_neighbors=3,metric = 'cosine', algorithm = 'brute')
model_knn.fit(recipe_features_df_matrix)

query_index = 24
distances, indices = model_knn.kneighbors(recipe_features_df.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 3)

for i in range(0, len(distances.flatten())):
    if i == 0:
        print('Recommendations for {0}:\n'.format(recipe_features_df.index[query_index]))
    else:
        print('{0}: {1}, with distance of {2}:'.format(i, recipe_features_df.index[indices.flatten()[i]], distances.flatten()[i]))