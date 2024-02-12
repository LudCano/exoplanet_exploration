## CLEANING DATA SCRIPT
## by L. Cano
## February 2024

import pandas as pd

## Reading all exoplanets
d = pd.read_csv("all_exoplanets.csv", skiprows=96)
print(d.columns)
