def task1():
     import csv
     import json
     import pandas as pd
     # load csv file
     data = pd.read_csv("/course/data/dataset.csv")
     # get unique data size separately
     task1 = {"Number of Products:":data['product_name'].unique().size, "Number of Categories:":data['category'].unique().size}
     # save the data as json file
     with open("task1.json","w") as f:
          json.dump(task1,f)
     return

     




     
     
     
   
