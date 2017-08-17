# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import collections
import numpy as np
import pandas as pd

def similarVectors1(a,b):
    a.sort()
    b.sort()
    print np.array_equal(a,b)
    
def similarVectors2(a,b):
    counters_a = collections.Counter(a)
    counters_b = collections.Counter(b)
    print counters_a == counters_b


a = np.empty((0))
b = np.empty((0))
for j in range(2):
    for i in range(1,11):
        a = np.append(a, i)
        b = np.append(b, 11-i)
        
def df_to_sarray(df):
    """
    Convert a pandas DataFrame object to a numpy structured array.
    This is functionally equivalent to but more efficient than
    np.array(df.to_array())

    :param df: the data frame to convert
    :return: a numpy structured array representation of df
    """

    v = df.values
    cols = df.columns

    types = [(cols[i].encode(), df[k].dtype.type) for (i, k) in enumerate(cols)]
    dtype = np.dtype(types)
    z = np.zeros(v.shape[0], dtype)
    for (i, k) in enumerate(z.dtype.names):
        z[k] = v[:, i]
    return z


"""print a
print b
similarVectors2(a,b)"""

#Read data from csv
data = pd.read_csv('sample.csv', delimiter = ';')
aux2 = df_to_sarray(data.reset_index())
aux = np.array(data)
keysArray = []
print aux
for i in range(len(data.keys())-1):
    keysArray.append(data.keys()[i])
keysArray = np.asarray(keysArray)
aux = np.insert(a,0,keysArray)
print aux

"""
keys = data.keys()
#Convert dataFrame to numpy array
a = data.values()
print a
#Convert numpy array to dataFrame
a2 = pd.DataFrame(sa)
#Convert DataFrame to csv
a2.to_csv("new_sample.csv")
print a2
"""
