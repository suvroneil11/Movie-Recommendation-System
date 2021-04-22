#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 02:35:35 2018

@author: suvroneil.11
"""

import json
import numpy as np

def pearson_score_calc(dataset,user1,user2):
    if user1 not in dataset:
        print(user1+" not found")
    if user2 not in dataset:
        print(user2+" not found")
    movies_ratings_by_both={}
    for movie in dataset[user1]:
        if movie in dataset[user2]:
            movies_ratings_by_both[movie]=1
    ratings = len(movies_ratings_by_both)
    if ratings<0:
        return 0
    user1_sum = np.sum([dataset[user1][movie] for movie in movies_ratings_by_both])
    user2_sum = np.sum([dataset[user2][movie] for movie in movies_ratings_by_both])
    user1_squared_sum = np.sum([np.square(dataset[user1][movie])for movie in movies_ratings_by_both])
    user2_squared_sum = np.sum([np.square(dataset[user2][movie])for movie in movies_ratings_by_both])       
    product_sum = np.sum([dataset[user1][movie] * dataset[user2][movie] for movie in movies_ratings_by_both])
    Sxy = product_sum - (user1_sum * user2_sum / ratings)
    Sxx = user1_squared_sum - np.square(user1_sum) / ratings
    Syy = user2_squared_sum - np.square(user2_sum) / ratings
    if Sxx * Syy == 0:
        return 0
    pearson_corl = Sxy / np.sqrt(Sxx * Syy)
    return pearson_corl

def finding_similar_users(dataset,user,number_of_users):
    score_list = np.array([[x, pearson_score_calc(dataset, user, x)] for x in dataset if user != x])
    sorted_scores_list= np.argsort(score_list[:, 1])
    descending_scores_sorted_list =sorted_scores_list[::-1]
    top = descending_scores_sorted_list[0:number_of_users]
    similar_name=score_list[top]
    return score_list[top]

def recommendations(dataset,user):
    total_scores = {}
    similarity_sums = {}

    for u in [x for x in dataset if x != user]:
        similarity_score = pearson_score_calc(dataset, user, u)

        if similarity_score <= 0:
            continue
        
        for item in [x for x in dataset[u] if x not in dataset[user] or dataset[user][x] == 0]:
            total_scores.update({item: dataset[u][item] * similarity_score})
            similarity_sums.update({item: similarity_score})

    if len(total_scores) == 0:
        return ['No recommendations possible']

    movie_ranks = np.array([[total/similarity_sums[item], item] 
            for item, total in total_scores.items()])

    movie_ranks = movie_ranks[np.argsort(movie_ranks[:, 0])[::-1]]
    recommendations = [movie for _, movie in movie_ranks]
    return recommendations

