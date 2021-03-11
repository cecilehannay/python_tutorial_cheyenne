from read_data import read_data

# This script the environment: conda activate python_tutorial
# ON the web: https://ncar.github.io/python-tutorial/tutorials/yourfirst.html#first-python-script
# on youtube: https://www.youtube.com/channel/UCoZPBqJal5uKpO8ZiwzavCw

# Column names and column indices to read
# created a column dict that points each data variable to its column-index. 
columns = {'date': 0, 'time': 1, 'temperature': 2, 'windspeed': 7, 'windchill': 12}

# Data types for each column (only if non-string)
types = {'temperature': float,'windspeed':float,'windchill':float}


# Initialize my datatable variable
# we initialize the dictionary in a loop 
# for each variable specified in columns, that key is initialized pointing to an empty list.
datatable = {}
for column in columns:
   datatable[column] = []

#############
# Read data from  CU Boulder Weather Station data file

datatable = read_data(columns, types=types)

###############


# Compute the wind chill temperature
def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v2 = v ** 0.16
    wci = a + (b * t) - (c * v2) + (d * t * v2)
    
    return(wci)


# Compute the wind chill factor
windchill = []
for temperature, windspeed in zip(datatable['temperature'], datatable['windspeed']):
    windchill.append(compute_windchill(temperature, windspeed))

# Debug
for windchill_computed, windchill_obs in zip( datatable['windchill'], windchill):
    print(windchill_computed, windchill_obs, windchill_computed-windchill_obs)


# Debug - formatted
for windchill_computed, windchill_obs in zip( datatable['windchill'], windchill):
    print(f'{windchill_computed:.2f}', f'{windchill_obs:.2f}', f'{windchill_computed-windchill_obs:.2f}')

