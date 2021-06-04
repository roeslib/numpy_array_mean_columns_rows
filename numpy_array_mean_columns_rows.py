import numpy as np

grades = np.array([[87, 96, 70],
                   [100, 87,90],
                   [94, 77, 90],
                   [100, 81, 82]])

#only working with the columns
columns_mean = grades.mean(axis = 0)

#only working with the rows
rows_mean = grades.mean(axis = 1)
