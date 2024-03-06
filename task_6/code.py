#!/usr/bin/env python3
# import library
import os; os.environ['TF_CPP_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import pandas as pd
url = 'https://raw.githubusercontent.com/mcstllns/DeepLearning/main/phone_price_classification_train.csv'
df = pd.read_csv(url)
df.head()
