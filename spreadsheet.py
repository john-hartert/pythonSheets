# Copy of spreadsheet here: https://docs.google.com/spreadsheets/d/1SnJhFzEFpMPCwYgSKQu3gVfDc3JCtBh8LRAQOiUibKo/edit#gid=152787366
# Shared this email with google sheets: legislators@python-sheets-180602.iam.gserviceaccount.com
# Installed: pip install gspread oauth2client

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# This uses credentials for API.
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# This opens the spreadsheet.
sheet = client.open("Copy of Legislators 2017").sheet1

# # Pulls all data.
# list_of_hashes = sheet.get_all_records()

# # Pulls row. (Left to right)
# list_of_hashes = sheet.row_values(1)

# # Pulls column. (Top to bottom)
# list_of_hashes = sheet.col_values(1)

# # Pulls cell.
# list_of_hashes = sheet.cell(2, 1).value

# # Writes to spreadsheet.
# list_of_hashes = sheet.update_cell(1, 1, "TEST TEST TEST TEST")

# # Inserts row. (Left to right)
# row = ["I'm", "inserting"]
# index = 1
# list_of_hashes = sheet.insert_row(row, index)

# # Deletes rows.
# list_of_hashes = sheet.delete_row(1)

# # Counts all rows.
list_of_hashes = sheet.row_count

print(list_of_hashes)

