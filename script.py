import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()


prev_orders=pd.read_csv('prev_orders.csv')
prev_orders.head()

from collections import defaultdict
from collections import Counter

user_dict = defaultdict(list)

for row in prev_orders.iterrows():
    row = row[1]
    user_dict[row["user_id"]].append(row["product_id"])
    
product_dict = []
for key in user_dict.keys():
    for j in user_dict[key]:
        if j not in product_dict:
            product_dict.append(j)
            print(j)

dict_list = []

for user_id in user_dict.keys():
    d = {"user_id":user_id}
    c = Counter(user_dict[user_id])
    print(c)
    d.update(c)
    dict_list.append(d)
    
user_ids = prev_orders['user_id'].unique()
product_ids = prev_orders['product_id'].unique()
dict_list = []

for user_id in user_ids:
    d = dict(zip(product_ids, [0]*len(product_ids)))
    d['user_id'] = user_id
    dict_sub = prev_orders[prev_orders['user_id']==user_id]['product_id'].value_counts().to_dict()
    d.update(dict_sub)
    dict_list.append(d)
print(dict_list[0])