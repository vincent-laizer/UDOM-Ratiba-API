from ratiba import ratiba, utils
import json

# FL1 = 3666
# FL2 = 3667
# LRB 105 = 3687
# LRB 106 = 3688
# Auditorium = 3663 

if __name__ == "__main__":
  academic_year = utils.get_current_academic_year()
  semester = ratiba.get_semesters(academic_year)[2]
  category = ratiba.get_categories(academic_year, semester)[0]
  option = ratiba.get_download_options(academic_year, semester, category)[0]
  # for option: 0 - venue, 1 - course, 2 - programme, 3 - instructor
  data = ratiba.get_data(academic_year, semester, category, option)[0]

  print(json.dumps(ratiba.get_timetable(academic_year, semester, category, option, data), indent=2))
