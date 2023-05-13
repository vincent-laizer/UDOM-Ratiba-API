import ratiba
import json

# FL1 = 3666
# FL2 = 3667
# LRB 105 = 3687
# LRB 106 = 3688
# Auditorium = 3663 

if __name__ == "__main__":
  # get timetable for LRB 106
  timetable = ratiba.get_timetable(venue_no=3688)
  print(json.dumps(timetable, indent=2))