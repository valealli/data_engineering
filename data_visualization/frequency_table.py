import pandas as pd
columnas = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
car_data = pd.read_csv("data_visualization/car.data", names=columnas)
print(car_data.info())
print(car_data.head())


def frequency_table(data:pd.DataFrame, col:str, column:str):
    freq_table = pd.crosstab(index=data[col],
                            columns=data[column],         
                            margins=True)
    rel_table = round(freq_table/freq_table.loc["All"], 2)
    return freq_table, rel_table

buying_freq, buying_rel = frequency_table(car_data, "class", "buying")

print("Two-way frequency table")
print(buying_freq)
print("---" * 15)
print("Two-way relative frequency table")
print(buying_rel)


import matplotlib.pyplot as plt
names = car_data["class"].value_counts().keys()
counts = car_data["class"].value_counts().values
plt.subplots(figsize=(8, 5))
plt.bar(names, counts, color="blue")
plt.xlabel("class names")
plt.ylabel("Frequency")
plt.title("Distribtuion of class")
plt.show()