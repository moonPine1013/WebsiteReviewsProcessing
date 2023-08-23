import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task7():
    # load json file
    with open('task6.json','r') as f:
        score_bigram_piars = json.load(f)
    positive_reviews_num = 0
    negative_reviews_num = 0

    # get all the bigrams
    bigrams_lst = []
    for score_bigram_piar in score_bigram_piars:
        for bigram_lst in score_bigram_piar.values():
            bigrams_lst = bigrams_lst + bigram_lst
    # then translate to a DataFrame,and drop duplicates
    df = pd.DataFrame({'bigram':bigrams_lst,'pos_num':0,'neg_num':0}).drop_duplicates()
    df = df.set_index('bigram')

    # count positive and negative reviews number
    # and count positive and negative number for each bigram
    for score_bigram_piar in score_bigram_piars:
        score_str = list(score_bigram_piar.keys())[0]
        if int (score_str) == 5:
            positive_reviews_num += 1
            bigram_lst = score_bigram_piar[score_str]
            bigram_set = set(bigram_lst)
            for bigram in bigram_set:
                df.loc[bigram,'pos_num'] += 1

        elif int(score_str) == 1:
            negative_reviews_num += 1
            bigram_lst = score_bigram_piar[score_str]
            bigram_set = set(bigram_lst)
            for bigram in bigram_set:
                df.loc[bigram,'neg_num'] += 1

    # remove the bigrams where positive and negative number is zero
    df = df[(df['pos_num'] != 0) & (df['neg_num'] != 0)]
    df['pos_prob'] = df['pos_num']/positive_reviews_num
    df['neg_prob'] = df['neg_num']/negative_reviews_num

    # caculate odds
    df['pos_odds'] = (df['pos_prob'].values/(1-df['pos_prob'].values))
    df['neg_odds'] = (df['neg_prob'].values/(1-df['neg_prob'].values))

    # caculate odds ratio
    df['odds_ratio'] = df['pos_odds']/df['neg_odds']

    # caculate log_odds_ratio
    df['log_odds_ratio'] = np.log10(df['odds_ratio'])

    df = df.sort_values('log_odds_ratio')

    df_saved = df[['log_odds_ratio']]
    df_saved.round(4).to_csv('task7a.csv')

    # task7b.png
    plt.figure()
    df_saved.groupby(pd.cut(df['log_odds_ratio'],bins=20)).size().plot(kind='bar')
    plt.title("distribution of log_odds_ratio for bigrams in the vocabulary")
    plt.subplots_adjust(bottom=0.4)
    plt.savefig('task7b.png')

    # task7c.png
    fig,axes = plt.subplots(1,2)
    df_saved.iloc[:10,:].plot(kind='bar',ax=axes[0],legend=False)
    df_saved.iloc[-10:,:].plot(kind='bar',ax = axes[1],legend=False)
    plt.subplots_adjust(bottom=0.45)
    fig.savefig('task7c.png')

    return

