# 
# Owen Morgan
# Oct. 22
# 

import module

def main()->None:
    location_data = []
    location = (input("Location (\"END to stop\"): "))
    while location != "END":
        sub_list = []
        sub_list.append(location)
        location_data.append(sub_list)
        location = (input("Location (\"END to stop\"): "))
    # print(location_data)
    air_data_compiled = module.assign_air_quality(location_data)
    air_data_sorted = sorted(air_data_compiled)
    print(air_data_sorted)
    # i = 0
    # while i <len(data_compiled):
    #     print(f"{i+1}. {data_compiled[i][0]} {data_compiled[i][1]} {data_compiled[i][2]}")
    #     i+=1
    mean = module.mean_calc(air_data_compiled)
    print(mean)
    median = module.median_calc(air_data_sorted)
    print(median)
    sorted_list = module.compare_air_quality(air_data_compiled,location_data)
    # print(sorted_list)
    
    
main()