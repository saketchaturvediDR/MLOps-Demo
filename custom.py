import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pickle

def transform(data, model):
    
    imputed_data = data.fillna(0)
    
    return imputed_data
