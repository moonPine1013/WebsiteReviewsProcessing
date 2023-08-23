import pandas as pd
import re
import numpy as np
def get_rating(reviewlist_str):
    '''helper function.get the average score for each product'''
    rate_pattern = re.compile(r'a-star-(\d{1}?)')
    rating_nums = []
    # use eval() to translate review string to python object
    for rating_str in [item['review_star'] for item in eval(reviewlist_str)]:
        # use re pattern to find the score
        rating_num = rate_pattern.findall(rating_str)
        if len(rating_num) > 0:
            rating_nums.append(int(rating_num[0]))
    # get the average of all scores
    if len(rating_nums) > 0:
        avg_rating = np.average(rating_nums)
    else:
        # print(reviewlist_str)
        avg_rating = 0
    return avg_rating
def task2():
    df = pd.read_csv('/course/data/dataset.csv')
    df_task2 = df[['ID','category']]
    # get average score
    df['average_score'] = df['REVIEWLIST'].apply(get_rating)
    df_task2 = df[['ID','category','average_score']]
    # sort by ID
    df_task2 = df_task2.sort_values('ID')
    
    # saved to csv file
    df_task2.to_csv('task2.csv',index=False)
    return
