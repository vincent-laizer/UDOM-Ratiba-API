# UDOM Ratiba API

## Overview
This project is designed to scrape data from the [ratiba.udom.ac.tz](https://ratiba.udom.ac.tz) website, which provides information about the academic schedules of the University of Dodoma in Tanzania. The scraped data includes the schedules of courses and other academic activities offered by the university.

The main purpose of this project is to provide users with a convenient way of accessing the university's academic schedule information by providing the scraped data in a structured format that can be easily parsed and analyzed.

## Dependencies
This project requires the following dependencies to be installed:
- Python 3.x
- Beautiful Soup 4
- Requests

## Installation
To install the project, follow these steps:
1. To get the latest version run,

```
pip install udomratibaapi
```

## Usage
Here is a list of all the functions provided and example usage for each

### Get Semesters
Function that returns all the semesters displayed in the ratiba website

This function accepts a dictionary of current academic year as a parameter and returns a list of dictionaries for each semester

```python
from udomratibaapi import ratiba, utils
import json

academic_year = utils.get_current_academic_year()
semesters = ratiba.get_semesters(academic_year)

# display the semesters
print(json.dumps(semesters, indent=2))
```

### Get Timetable Categories
Function that returns all the timetable categories from the site. Possible values include *Teaching* or *Test* timetables

This function accepts a dictionary of current academic year and a dictionary of semester

```python
from udomratibaapi import ratiba, utils
import json

academic_year = utils.get_current_academic_year()
semesters = ratiba.get_semesters(academic_year)

# pic one semester from the array
semester_two = semesters[2]
categories = ratiba.get_categories(academic_year, semester_two)

# display the categories
print(json.dumps(categories, indent=2))
```

### Get Download Options
Returns all the download options from the site. Possible values include *Venue*, *Course*, *Programme* and *Instructor*

This function accepts a dictionary of current academic year, semester of choice and category of choice

```python
from udomratibaapi import ratiba, utils
import json

academic_year = utils.get_current_academic_year()
semesters = ratiba.get_semesters(academic_year)

# pick one semester from the array
semester_two = semesters[2]
categories = ratiba.get_categories(academic_year, semester_two)

# pick one category, say Teaching
category = categories[0]

options = ratiba.get_download_options(academic_year, semester_two, category)

# display the options
print(json.dumps(options, indent=2))
```

### Get Option Data
This function gets the chioces for the specific option selected. Suppose you select venue in options, it will return a list of all venues present in the site

It accepts all the parameters of the **Get Download Options** function with an added one which is a dictionary of a particular option

```python
from udomratibaapi import ratiba, utils
import json

academic_year = utils.get_current_academic_year()
semesters = ratiba.get_semesters(academic_year)

# pick one semester from the array
semester_two = semesters[2]
categories = ratiba.get_categories(academic_year, semester_two)

# pick one category, say Teaching
category = categories[0]

options = ratiba.get_download_options(academic_year, semester_two, category)

# pick one option from the list of options (venues)
# for option: 0 - venue, 1 - course, 2 - programme, 3 - instructor
venue_option = options[0]
venues_list = ratiba.get_data(academic_year, semester, category, venue_option)

# display the option data (list of all venues)
print(json.dumps(venues_list, indent=2))
```

### Get Timetable
Finally combine all the data and choices from previous functions to get the whole timetable data based on your choices

```python
from udomratibaapi import ratiba, utils
import json

academic_year = utils.get_current_academic_year()
semesters = ratiba.get_semesters(academic_year)

# pick one semester from the array
semester_two = semesters[2]
categories = ratiba.get_categories(academic_year, semester_two)

# pick one category, say Teaching
category = categories[0]

options = ratiba.get_download_options(academic_year, semester_two, category)

# pick one option from the list of options (venues)
# for option: 0 - venue, 1 - course, 2 - programme, 3 - instructor
venue_option = options[0]
venues_list = ratiba.get_data(academic_year, semester_two, category, venue_option)

# select one specific venue
# LRB 106 is a venue from CIVE, UDOM and has an id of 3688
lrb_106 = [v for v in venues_list if v['id'] == "3688"][0]

# get timetable for the choose venue
timetable = ratiba.get_timetable(academic_year, semester_two, category, venue_option, lrb_106)

# display the timetable
print(json.dumps(timetable, indent=2))
```

*Its important to go through [UDOM Ratiba site](https://ratiba.udom.ac.tz) carefully to understand these functions*

## Contribution
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. 

## Credits
This project was created by [VincentLaizer](https://github.com/vincent-laizer). 

## License
This project is licensed under the [MIT]() license.