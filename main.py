from ratiba import ratiba, utils
import json

# FL1 = 3666
# FL2 = 3667
# LRB 105 = 3687
# LRB 106 = 3688
# Auditorium = 3663 

if __name__ == "__main__":
  curr_ac_yr = utils.get_current_academic_year()
  semesters = ratiba.get_semesters(curr_ac_yr)
  # print(json.dumps(ratiba.get_semesters(curr_ac_yr), indent=2))
  print(json.dumps((ratiba.get_categories(curr_ac_yr, semester)), indent=2))