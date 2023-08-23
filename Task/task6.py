import pandas as pd
import re
import json
from nltk.corpus import stopwords

def task6():
    stop_words = set(stopwords.words('english'))
    df = pd.read_csv('/course/data/dataset.csv')
    result = []
    for _,row in df.iterrows():
        reviewlist = eval(row['REVIEWLIST'])
        for item in reviewlist:
            # preprocess
            review_str = item['review_body']
            score_str = item['review_star']
            rate_pattern = re.compile(r'a-star-(\d{1}?)')
            reviews_non_alphabetic_pattern = re.compile(r"([^\w]+)")
            # substitute all non-alphabet character by space using re pattern
            review_str = reviews_non_alphabetic_pattern.sub(' ',review_str).lower()
            review_lst = []
            # remove stopwords
            for word in review_str.split(' '):
                if word not in stop_words and len(word) > 2:
                    review_lst.append(word)
            # bigram
            bigram_lst = [' '.join([review_lst[idx],review_lst[idx+1]]) for idx in range(len(review_lst) -1 )]

            # score
            rating_num = rate_pattern.findall(score_str)
            if len(rating_num) > 0:
                rating_num = int(rating_num[0])
            else:
                rating_num = 0
            # save json
            if rating_num != 0 and len(bigram_lst) > 0:
                score_bigram_piar = {rating_num:bigram_lst}
                result.append(score_bigram_piar)
    with open('task6.json','w') as f:
        json.dump(result,f)
    return
