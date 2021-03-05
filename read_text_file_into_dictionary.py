# This script the environment: conda activate python_tutorial

# Initialize data variable
datatable = {'date': [ ],
    'time':[],
    'temperature': []}


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
    datatable['date'].append(row[0])
    datatable['time'].append(row[1])
    datatable['temperature'].append(float(row[2]))

# print for debug
print(datatable['temperature'])

# close file
datafile.close()
