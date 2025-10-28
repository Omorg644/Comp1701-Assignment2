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
    print(location_data)
    data_compiled = module.assign_air_quality(location_data)
    print(data_compiled)
    # i = 0
    # while i <len(air_data):
    #     print(f"{i+1}. {air_data[i][0]} {air_data[i][1]} {air_data[i][2]}")
    #     i+=1
    # mean = module.mean_calc(air_data)
    # print(mean)
    # median = module.median_calc(air_data)
    # print(median)
    
    
main()