import pandas as pd
import matplotlib.pyplot as plt


d = pd.read_csv("data/data.csv")

#print(d.columns)
methods = d.discoverymethod.unique()
print(methods)
method_groups = []
for i in methods:
    df = d[d.discoverymethod == i]
    method_groups.append(df)
    print(i, "--->", len(df), " exoplanets")

