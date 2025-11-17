# 
# Owen Morgan
# COMP 1701 Assignment 2
# Nov. 16
# 

import module

GOOD_AIR_CUTOFF = 50 #[3]

def main()->None:
    location_data = ["Airdrie","Calgary Varsity","Caroline","Edson","Elk Island","Jasper","Fort Chipewyan","St. Albert","Wapasu","Smoky Heights"] #[3]
    june_data_unsorted = [141,153,136,50,73,98,9,79,14,40] #[3]
    month_oct = False
    june_data_compiled = module.assign_air_quality(location_data,june_data_unsorted,month_oct)
    june_data_sorted = sorted(june_data_unsorted) #[1]
    # print(june_data_sorted)
    # print(june_data_compiled)

    month_oct = True
    oct_data_compiled = module.assign_air_quality(location_data,june_data_unsorted,month_oct)
    oct_data_unsorted = oct_data_compiled[1]
    # print(oct_data_compiled)
    oct_data_sorted = sorted(oct_data_unsorted) #[1]
    # print(oct_data_sorted)

    june_mean = module.mean_calc(june_data_unsorted)
    # print(june_mean)
    oct_mean = module.mean_calc(oct_data_unsorted)
    # print(oct_mean)

    june_median = module.median_calc(june_data_sorted)
    # print(june_median)
    oct_median = module.median_calc(oct_data_sorted)
    # print(oct_median)

    june_compared_list = module.compare_air_quality(june_data_compiled,june_data_sorted)
    # print(june_compared_list)
    oct_compared_list = module.compare_air_quality(oct_data_compiled[0],oct_data_sorted)
    # print(oct_compared_list)

    june_good_percent = module.find_percent(june_data_sorted,GOOD_AIR_CUTOFF)
    # print(june_good_percent)
    oct_good_percent = module.find_percent(oct_data_sorted,GOOD_AIR_CUTOFF)
    # print(oct_good_percent)
    
    module.display_list(location_data,june_data_unsorted,oct_data_unsorted)
    module.display_data(june_mean,june_median,june_good_percent,june_compared_list,month="June")
    module.display_data(oct_mean,oct_median,oct_good_percent,oct_compared_list,month="October")

main()

# Reference List
# [1] "Why does "return list.sort()" return None, not the list? [duplicate]", stackoverflow. [Online]. Available: https://stackoverflow.com/questions/7301110/why-does-return-list-sort-return-none-not-the-list
# [2] "Median", Wikipedia. [Online]. Available: https://en.wikipedia.org/wiki/Median
# [3] P. Perri. “Assignment 2. Hypothesis Testing – Decomposing a problem into abstractions, coded with functions.” COMP 1701, Mount Royal University, Fall 2025. [Online]. Available: https://learn.mymru.ca