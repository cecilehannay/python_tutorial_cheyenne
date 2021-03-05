# Initialize data variable
datatable = [ ]

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
    datatable.append(row)
    

# print for debug
print(row)

# close file
datafile.close()
