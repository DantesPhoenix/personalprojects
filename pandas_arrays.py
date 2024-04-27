# import pandas library
import pandas as pd

def array():
    #define array
    dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
           "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
           "area (million km²)": [8.516, 17.10, 3.286, 9.597, 1.221],
           "population (million)": [200.4, 143.5, 1252, 1357, 52.98] }

    brics = pd.DataFrame(dict)

    # Set the index for brics
    brics.index = ["BR", "RU", "IN", "CH", "SA"]

    # Print out brics with new index values
    print(brics)

#main program
array()