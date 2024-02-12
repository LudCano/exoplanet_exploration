import pandas as pd

# READING DATA
data = pd.read_csv("data/data_trimmed.csv", skiprows=40)
hwc = pd.read_csv("data/hwc_hab.csv")

#print(len(data))
#print(hwc.columns)
c = 0
hab_vec = []
for i in data.pl_name.to_list():
    if i in hwc.Name.to_list():
        #print(i, "found")
        c += 1
        hab_vec.append(1)
    else:
        hab_vec.append(0)
print(c)

data["hwc"] = hab_vec
data.to_csv("data/data.csv", index=False)
