### 1. Read in JSON File

import ijson

filename = "C:\Users\gordon-local\Downloads\json_montgomerycountymd_gov.json"

with open(filename, 'r') as f:
    objects = ijson.items(f, 'meta.view.columns.item')
    columns = list(objects)


### 2. Print Columns

print(columns[0])   # print first array of data
column_names = [col["fieldName"] for col in columns]    # list columns
column_names


### 3.  Select the useful columns and read in those data. This will reduce the memory used.

good_columns = [
    "date_of_stop", 
    "time_of_stop", 
    "agency", 
    "subagency",
    "description",
    "location", 
    "latitude", 
    "longitude", 
    "vehicle_type", 
    "year", 
    "make", 
    "model", 
    "color", 
    "violation_type",
    "race", 
    "gender", 
    "driver_state", 
    "driver_city", 
    "dl_state",
    "arrest_type"
]


data = []
with open(filename, 'r') as f:
    objects = ijson.items(f, 'data.item')
    for row in objects:
        selected_row = []
        for item in good_columns:
            selected_row.append(row[column_names.index(item)])
        data.append(selected_row)