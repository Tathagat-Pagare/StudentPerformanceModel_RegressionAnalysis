# Import Data Manipulation Libraries

import numpy as np
import pandas as pd

# Import Data Visualization Libraries

import matplotlib.pyplot as plt
import seaborn as sns

# Import Data Warning Libraries

import warnings
warnings.filterwarnings(action='ignore')


#1. Function Defining

filepath = 'https://raw.githubusercontent.com/Tathagat-Pagare/StudentPerformanceModel_RegressionAnalysis/refs/heads/main/data/Student_Performance.csv'

# Step1 = Data Ingestion 

def data_ingestion():
    return pd.read_csv(filepath)

#Step2 = Descriptive Stats

def data_exploration(df):
    pass

#Step3 = Pre-processing

def data_preprocessing(df):
    pass

#Step4 = Model Building

def model_building(df):
    pass

#2. Function Calling 

df = data_ingestion()

data_exploration(df)

data_preprocessing(df)

model_building(df)

#Test df
print(df)