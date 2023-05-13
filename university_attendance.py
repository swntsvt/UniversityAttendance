import itertools
from functools import reduce

def university_attendance(number_of_days):
    
    # generate truth table inputs for combinations of attendances
    all_combinations = list(itertools.product([1, 0], repeat=number_of_days))

    eligible_for_graduation_list = list()
    missing_graduation_list = list()

    four_consecutive_absences = "0000"

    for combination in all_combinations:
        # check if there are four consecutive absences
        if four_consecutive_absences in "".join(str(i) for i in combination):
            eligible_for_graduation_list.append(0)
        else:
            eligible_for_graduation_list.append(1)
    
    eligible_for_graduation_count = reduce(lambda a,b: a + b, eligible_for_graduation_list)

    for i in range(len(all_combinations)):
        # missing graduation check - 2 conditions - eligible for graduation but absent on n'th day
        if all_combinations[i][-1] == 0 and eligible_for_graduation_list[i] == 1:
            missing_graduation_list.append(1)
        else:
            missing_graduation_list.append(0)
            
    missing_graduation_count = reduce(lambda a,b: a + b, missing_graduation_list)
    
    final_result = str(missing_graduation_count) + "/" + str(eligible_for_graduation_count) 
    return final_result
    
number_of_days = 10
result_str = university_attendance(number_of_days)
print(result_str)   