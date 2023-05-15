from ratiba import ratiba, utils
import json

# FL1 = 3666
# FL2 = 3667
# LRB 105 = 3687
# LRB 106 = 3688
# Auditorium = 3663 

if __name__ == "__main__":
  print(json.dumps(ratiba.get_semesters(), indent=2))