import requests
from bs4 import BeautifulSoup
import json

def get_timetable(venue_no:int):
  ''' Get timetable for a venue '''
  # get data from udom servers
  url = f"https://ratiba.udom.ac.tz/index.php/downloads/view?year=9&semester=3352&type=1&option=room&data[]={venue_no}"
  response = requests.get(url)

  # parse the resulting HTML
  soup = BeautifulSoup(response.text, 'html.parser')
  table = soup.find('table', {'class': 'table'})
  rows = [[td.text.strip() for td in tr.find_all('td')] for tr in table.find_all('tr') if tr.find_all('td')]

  ratiba = []
  days = {}
  sessions = []
  prev_day = rows[0][0]

  # create a custom json object i can work with
  for index, row in enumerate(rows):
    if str(row[0]) != '' and index != 0:
        days["day"] = prev_day
        days["sessions"] = sessions
        prev_day = row[0]

        if index < len(rows)-1:
            ratiba.append(days)
            sessions = []
            days = {}

    if str(row[1]) == "":
        time = str(prev_time)
    else:
        time = str(row[1])
        prev_time = row[1]

    start_time = time.split("-")[0].strip()
    end_time = time.split("-")[1].strip()

    sessions.append({
        "start_time": start_time,
        "end_time": end_time,
        "course": row[2],
        "venue": row[3],
        "instructor": row[4],
        "students": row[5]
    })

    if index == len(rows)-1:
        days["day"] = prev_day
        days["sessions"] = sessions
        ratiba.append(days)

  return ratiba
