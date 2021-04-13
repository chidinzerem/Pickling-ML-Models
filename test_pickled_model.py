#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

import pickle
import json 


# In[7]:


from newdata import newdata
newdata = newdata

with open('model.pkl', 'rb') as f:
  newdata = pickle.load(f)

predictions = pipe.predict_proba(newdata)
print(predictions)


# In[ ]:




