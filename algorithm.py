# 
# Owen Morgan
# Oct. 22
# 

import module

def main()->None:
    # location_data = []
    # location = (input("Location (\"END to stop\"): "))
    # while location != "END":
    #     sub_list = []
    #     sub_list.append(location)
    #     location_data.append(sub_list)
    #     location = (input("Location (\"END to stop\"): "))
    # print(location_data)
    # air_data_compiled = module.assign_air_quality(location_data)
    # air_data_unsorted = air_data_compiled[1]
    # print(air_data_unsorted)
    # air_data_sorted = sorted(air_data_unsorted)
    # print(air_data_sorted)
    # mean = module.mean_calc(air_data_unsorted)
    # print(mean)
    # median = module.median_calc(air_data_sorted)
    # print(median)

    # compared_list = module.compare_air_quality(air_data_compiled[0],air_data_sorted)
    test_location = [['q', 1], ['w', 2], ['e', 3], ['r', 4], ['t', 5], ['y', 6], ['u', 7], ['i', 8], ['o', 9], ['p', 0]]
    test_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    compared_list = module.compare_air_quality(test_location,test_sorted)
    print(compared_list)
    
    
main()