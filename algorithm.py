# 
# Owen Morgan
# Oct. 22
# 

import module

GOOD_AIR_CUTOFF = 50

def main()->None:
    location_data = []
    location = (input("Location (\"END to stop\"): "))
    while location != "END":
        sub_list = []
        sub_list.append(location)
        location_data.append(sub_list)
        location = (input("Location (\"END to stop\"): "))
    print(location_data)
    # month = 
    # either put all functions in loop with each iteration passing june or oct as param, or have all functions in a seperate moule function with ,onsths as a param
    air_data_compiled = module.assign_air_quality(location_data, month)
    air_data_unsorted = air_data_compiled[1]
    print(air_data_unsorted)
    air_data_sorted = sorted(air_data_unsorted)
    print(air_data_sorted)

    mean = module.mean_calc(air_data_unsorted)
    print(mean)

    median = module.median_calc(air_data_sorted)
    print(median)

    # test_location = [['q', 1], ['w', 2], ['e', 3], ['r', 4], ['t', 0], ['y', 0], ['u', 0], ['i', 8], ['o', 7], ['p', 9]]
    # test_sorted = [0, 0, 0, 1, 2, 3, 4, 7, 8, 9]
    compared_list = module.compare_air_quality(air_data_compiled[0],air_data_sorted)
    print(compared_list)

    # test_sorted = [10, 20, 50, 100, 250, 300, 400, 700, 800, 900]
    good_percent = module.find_percent(air_data_sorted,GOOD_AIR_CUTOFF)
    print(good_percent)
    

    
main()