import numpy as np
import pandas as pd
import time

np.random.seed(2)

N_STATES = 6
ACTIONS = ['left','right']
EPSILON = 0.9 #GREEDY POLICY
ALPHA = 0.1 #LEARNING RATE
LAMBDA = 0.9 #DISCOUNT FACTOR
MAX_EPSODES = 13
FRESH_TIME = 0.3

print('hello world')