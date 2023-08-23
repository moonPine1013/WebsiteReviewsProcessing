import pandas as pd
import matplotlib.pyplot as plt
def task5():
    rating_df = pd.read_csv('task2.csv',index_col=0)
    rating_df.groupby('category').mean().sort_values('average_score').plot(kind='bar')
    
    plt.xticks(rotation=90)
    plt.title("""the means of the average review scores 
    of products in each category""")
    plt.subplots_adjust(bottom=0.52)
    plt.savefig('task5.png')
