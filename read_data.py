def read_data(columns, types={}, filename = "data/wxobs20170821.txt"):
    """
    Read data from CU Boulder Weather Station data file

   Parameters:
      columns: A dictionary of column names mapping to column indices
      types: A dictionary of column names mapping to types to which
         to convert each column of data
      filename: The string path pointing to the CU Boulder Weather
            Station data file
    """
     
    # Initialize my datatable variable
    # we initialize the dictionary in a loop 
    # for each variable specified in columns, that key is initialized pointing to an empty list.
    datatable = {}
    for column in columns:
        datatable[column] = []


    # open the data file
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

return data
