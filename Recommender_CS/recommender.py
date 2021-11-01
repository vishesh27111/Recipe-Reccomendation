import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def combine_features(row):
    return row['Course'] + " " + row['Cuisine'] + " " + row['Diet']


def recommender():
    df = pd.read_csv('/Users/aryan/Desktop/Python/yolo_v5/Flask_API/Recommender_CS/clean_data.csv')
    print(df.columns)

    features = ['Course', 'Cuisine', 'Diet']
    df['combined_features'] = df.apply(combine_features, axis=1)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])
    cosine_sim = cosine_similarity(count_matrix)
    dish_user = 'Masala Karela Recipe'

    recipe_index = get_index_from_name(dish_user, df) - 1
    similar_recipe = list(enumerate(cosine_sim[recipe_index]))
    sorted_similar_recipe = sorted(similar_recipe, key=lambda x: x[1], reverse=True)
    i = 0
    recommendations = []
    for recipe in sorted_similar_recipe:
        final = get_name_from_index(recipe[0], df)
        recommendations.append(final)
        print(final)
        i = i + 1
        if i > 20:
            break

    return recommendations


def get_name_from_index(index, df):
    return df[df.index == index]['RecipeName'].values[0]


def get_index_from_name(title, df):
    return df[df.RecipeName == title]['Srno'].values[0]


if __name__ == '__main__':
    recommendations = recommender()
    print(recommendations)
