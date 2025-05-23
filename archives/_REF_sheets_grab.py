import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from tabulate import tabulate

KEYFILE = r"C:\Users\stone\Desktop\frostfire-460722-348a7b25473a.json"

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(KEYFILE, scope)
client = gspread.authorize(creds)

spreadsheet = client.open("Frostfire")
worksheet = spreadsheet.sheet1
pairs = worksheet.get("B8:C14")
engine_specs = {row[0]: row[1] for row in pairs if len(row) == 2}
df = pd.DataFrame(engine_specs.items(), columns=["Parameter", "Value"])

print(tabulate(df, headers="keys", tablefmt="fancy_grid"))
