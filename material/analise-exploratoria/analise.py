import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# RAG2124.csv EXCLUÍDO PORQUE ERA PESADO DEMAIS

# file_path = '../datasets/RAG2124.csv' 
# data = pd.read_csv(file_path, sep=';', encoding='latin1', low_memory=False)

# rj_data = data[data['SG_UF'] == 'RJ']

# rj_data.to_csv('../datasets/RAG2124_RJ.csv', sep=';', index=False, encoding='latin1') 

# file_path = '../datasets/RAG2124_RJ.csv'
# data = pd.read_csv(file_path, sep=';', encoding='latin1', low_memory=False)

# data_cleaned = data.dropna(axis=1)

# data_cleaned.to_csv('../datasets/RAG2124_RJ_cleaned.csv', sep=';', index=False, encoding='latin1')

file_path = '../datasets/RAG2124_RJ_cleaned.csv'
data = pd.read_csv(file_path, sep=';', encoding='latin1', low_memory=False)

print(data.head())
