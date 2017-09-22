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

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

