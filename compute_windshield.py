# This script the environment: conda activate python_tutorial

# Column names and column indices to read
# created a column dict that points each data variable to its column-index. 
columns = {'date': 0, 'time': 1, 'temperature': 2, 'windspeed': 7}

# Data types for each column (only if non-string)
types = {'temperature': float,'windspeed':float}


# Initialize my datatable variable
# we initialize the dictionary in a loop 
# for each variable specified in columns, that key is initialized pointing to an empty list.
datatable = {}
for column in columns:
   datatable[column] = []


# open the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, "r")

# skip the 3 first lines
# Because the variable _ is never called in the loop we just call it: _
for _ in range(3):
    datafile.readline()

# read line by line
# Use the concept of split() and append()
for line in datafile:
    row = line.split()
    for column in columns:
        i = columns[column]
        t = types.get(column, str)
        value = t(row[i])
        datatable[column].append(value)

# close file
datafile.close()

# Compute the wind chill temperature
def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v2 = v ** 2
    wci = a + (b * t) - (c * v2) + (d * t * v2)
    
    return(wci)


# Compute the wind chill factor
windchill = []
for temperature, windspeed in zip(datatable['temperature'], datatable['windspeed']):
    windchill.append(compute_windchill(temperature, windspeed))
