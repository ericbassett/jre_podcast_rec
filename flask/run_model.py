from copy import deepcopy
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import linear_kernel
import pickle

my_recommender = pickle.load(open('data/recommender.pickle','rb'))
    

