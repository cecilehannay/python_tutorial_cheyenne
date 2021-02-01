# read the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')

data = datafile.read() 

datafile.close()

# DEBUG
print(type(data))




