import matplotlib.pyplot as plt
import pandas as pd

def task4():
    rating_df = pd.read_csv('task2.csv')
    cost_df = pd.read_csv('task3.csv')
    total_df = pd.merge(rating_df.drop('category',axis=1),cost_df,on='ID')
    total_df = total_df.set_index('ID')

    # select the category Pet Supplies
    total_df = total_df[total_df['category']=='Pet Supplies']
    plt.figure(figsize = (10,12))
    total_df.plot.scatter(x='average_cost',y='average_score')
    plt.title("""the average price with the 
    average review score for each product in 'Pet Supplies'""")
    plt.subplots_adjust(bottom=0.2)
    plt.savefig('task4.png')
