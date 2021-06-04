import numpy as np

grades = np.array([[87, 96, 70],
                   [100, 87,90],
                   [94, 77, 90],
                   [100, 81, 82]])

#only working with the columns
columns_mean = grades.mean(axis = 0)

#only working with the rows
rows_mean = grades.mean(axis = 1)

#Exercise: Use NumPy random-number generation to create an array of 
#twelve random grades in the range 60 through 100, then reshape the 
#result into a 3-by-4 array. Calculate the average of all the grades,
#the averages of the grades in each column and the averages of the grades
#in each row

#mean with all the values from the array
np.random.randint(60,101,12).reshape(3,4).mean()

#mean with the values from the columns
np.random.randint(60,101,12).reshape(3,4).mean(axis=0)

#mean with the values from the rows
np.random.randint(60,101,12).reshape(3,4).mean(axis=1)
