import pandas as pd
data = pd.read_csv('features_data.csv')
type(data)
import numpy as np
t = np.linspace(4, 12, 10)
sin_t = np.sin(t)
cos_t = np.cos(t)
numbers = pd.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})
print(numbers)
print(numbers.shape)
print(numbers.columns)
print(data.columns)
print(numbers['t'][0:20])
data[data['t']]