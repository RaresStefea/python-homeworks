from .functions import file_copy, word_count
from .database_csv import (
    init_db,
    add_record,
    view_records,
    search_record,
    delete_record,
)
from .database_json import (
    init_db as json_init,
    add_record as json_add,
    view_records as json_view,
    search_record as json_search,
    delete_record as json_delete,
    update_record,
)
import re

"""
print("File copy")
print("Path of source:")
source = input().strip()

print("Path of destination:")
destination = input().strip()

file_copy(source, destination)

word_count(source)
"""

"""
print("CSV Database Operations:")
csvpath = input().strip()

init_db(csvpath)

print("Add a row(id,name,age,city):")
new_row = input().strip()

worked_row = re.split(r"[,;\s]+", new_row)

if len(worked_row) == 4:
    worked_row[0] = int(worked_row[0])
    add_record(csvpath, *worked_row)
else:
    raise NotImplementedError

print("The records are:")
view_records(csvpath)

print("Record search, enter the search term:")
search_term = input().strip()
search_record(csvpath, search_term)

print("Delete a record, enter record delete term:")
delete_term = input().strip()
delete_record(csvpath,delete_term)
"""

print("JSON Database Operations:")
jsonpath = input().strip()

json_init(jsonpath)

print("Add a row(name,age,city):")
new_row = input().strip()


worked_row = re.split(r"[,;\s]+", new_row)
worked_row[1] = int(worked_row[1])

if len(worked_row) == 3:
    json_add(jsonpath, *worked_row)
else:
    raise NotImplementedError

json_view(jsonpath)

print("Record search, enter the search term:")
search_term = input().strip()
json_search(jsonpath, search_term)

print("Delete a record, enter record delete term:")
json_delete_word = input().strip()
json_delete(jsonpath, json_delete_word)

print("Update a value, enter the id:")
id = int(input().strip())
print("Enter the value:")
new_value = input().strip()
print("Enter the key for the value:")
key = input().strip()
update_record(jsonpath, id, key, new_value)
