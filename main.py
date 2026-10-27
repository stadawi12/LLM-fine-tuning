import pandas as pd
from io import BytesIO

import torch

# <class 'pandas.core.frame.DataFrame'>
train_df = pd.read_parquet('data/train.parquet')  
test_df = pd.read_parquet('data/test.parquet')
val_df = pd.read_parquet('data/val.parquet')

# Print the number of examples in each DataFrame
print("Number of examples in train_df:", len(train_df))
print("Number of examples in test_df:", len(test_df))
print("Number of examples in val_df:", len(val_df))

article_example = 1
article_fact = 1

article_text_example = train_df["text"].iloc[article_example]

print(article_text_example[article_fact]) # Output: <class 'str'>