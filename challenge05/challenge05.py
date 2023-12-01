import csv
import re

database = open("database_attacked.txt")

valid_rows = []
invalid_rows = []

for row in csv.reader(database, delimiter=","):
    id = row[0]
    username = row[1]
    email = row[2]
    age = row[3]
    location = row[4]

    if not id.isalnum():
        invalid_rows.append(row)
        continue

    if not username.isalnum():
        invalid_rows.append(row)
        continue

    if not re.match(r"^\w+@\w+\.com$", email):
        invalid_rows.append(row)
        continue

    if not age.isdigit():
        invalid_rows.append(row)
        continue

    if location != "" and not location.replace(" ", "").isalpha():
        invalid_rows.append(row)
        continue

    valid_rows.append(row)

message = ""

for row in invalid_rows:
    print(row)
    username = row[1]
    if username != "":
        message += username[0]

print(message)
open("output_05.txt", "w").write(message)
