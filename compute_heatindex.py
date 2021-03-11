from read_data import read_data

# This script the environment: conda activate python_tutorial
# ON the web: https://ncar.github.io/python-tutorial/tutorials/yourfirst.html#first-python-script
# on youtube: https://www.youtube.com/channel/UCoZPBqJal5uKpO8ZiwzavCw

# Column names and column indices to read
# created a column dict that points each data variable to its column-index. 
columns = {'date': 0, 'time': 1, 'temperature': 2, 'humidity': 5, 'heatindex': 13}

# Data types for each column (only if non-string)
types = {'temperature': float,'humidity':float,'heatindex':float}

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

 # Compute the heat index
def compute_heatindex(t, rh_pct):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = -0.22475541
    e = -0.00683783
    f = -0.05481717
    g = 0.00122874
    h = 0.00085282
    i = -0.00000199

    rh = rh_pct / 100

    hi = a + (b * t) + (c * rh) + (d * t * rh)
    + (e * t**2) + (f * rh**2) + (g * t**2 * rh)
    + (h * t * rh**2) + (i * t**2 * rh**2)
    return hi


# Compute the heat index
heatindex = []
for temperature, humidity in zip(datatable['temperature'], datatable['humidity']):
    heatindex.append(compute_heatindex(temperature, humidity))

# Output
print('------- ------  -----  ----- ------')
print(' Date    Time   HIcomp HIobs  Diff ')
print('------- ------  -----  ----- ------')
for date, time, heatindex_computed, heatindex_obs in zip(datatable['date'], datatable['time'], datatable['heatindex'], heatindex):
    print(f'{date} {time} {heatindex_computed:6.2f} {heatindex_obs:6.2f} {heatindex_computed-heatindex_obs:6.2f}')

