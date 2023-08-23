import pandas as pd
import re
import numpy as np
def get_cost(cost_str:str):
    '''helper function.get the everage cost for each product'''
    digits_pattern = re.compile(r'(\d+\.{0,1}\d*)')
    # remove comma
    cost_str = cost_str.replace(',','')
    # find all costs use re pattern
    costs = digits_pattern.findall(cost_str)
    result = 0
    if len(costs) == 1:
        result =  float(costs[0])
    elif len(costs) == 2:
        result =  (float(costs[0]) + float(costs[1])) / 2
    else:
        # print(costs,cost_str)
        result = 0
    return round(result,2)
def task3():
    df = pd.read_csv('/course/data/dataset.csv')
    df_task2 = df[['ID','category']]
    df['average_cost'] = df['cost'].apply(get_cost)
    df_task2 = df[['ID','category','average_cost']]
    df_task2 = df_task2.sort_values('ID')
    df_task2.to_csv('task3.csv',index=False)
    return
