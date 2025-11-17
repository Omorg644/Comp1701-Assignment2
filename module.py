# 
# Owen Morgan
# COMP 1701 Assignment 2
# Nov. 16
# 

def mean_calc(air_data:list)->float:
    """Find the mean from a list of air quality data"""
    i = 0
    sum = 0
    while i < len(air_data):
        sum+=air_data[i]
        i+=1
    sum = sum/len(air_data)
    # print(sum)
    return sum
    
def median_calc(air_data:list)->float:
    """Find the median from a list of air quality data"""
    # print(air_data)
    # print(len(air_data))
    if (len(air_data)%2)==0:
        middle = (air_data[len(air_data)//2] + air_data[(len(air_data)//2)-1])/2 #[2]
        # print(air_data[len(air_data)//2], air_data[(len(air_data)//2)-1])
    else:
        middle = air_data[((len(air_data)+1)//2)] #[2]
        # print(((len(air_data)+1)//2))
    return middle

def assign_air_quality(location_data:list,june_data:list,user_input:bool)->list:
    """Assign air qaulity data to location names"""
    i = 0
    air_data = []
    location_air_data = []
    data_compiled = []
    if not user_input: 
        while i<len(location_data):
            data_compiled.append([location_data[i], june_data[i]])
            i+=1
    else:
        j=0
        while j <len(location_data):
            data_oct = int(input(f"{location_data[j]}'s air quality in october: "))
            air_data.append(data_oct)
            location_air_data.append([location_data[j], data_oct])
            j+=1
    if user_input:
        data_compiled.append(location_air_data) 
        data_compiled.append(air_data)
    return data_compiled

def compare_air_quality(location_data:list, sorted_data:list)->list:
    """Return a list of the locations with the worst air quality"""
    # print(location_data)
    # print(sorted_data)

    sorted_list = []
    i=0
    while i<len(location_data):
        # print("hi hello")
        j=2 
        while j >= 1:
            # print("hello")
            if location_data[i][1]==sorted_data[-1*j] and not location_data[i][0] in sorted_list:
                # print("hi")
                sorted_list.append(location_data[i])
            j-=1
            
        i+=1
        # if 
    # print(sorted)
    return sorted_list

def find_percent(num_list:list,comparison:int)->float:
    """Return the percentage of items that are above a specified value"""
    greater_than = []
    i = 0
    while i < len(num_list):
        if num_list[i] >= comparison:
            greater_than.append(num_list[i])
        i+=1
    percent = 100 - ((len(greater_than)/len(num_list))*100)
    return percent

def display_list(location:list,june:list,oct:list)->None:
    """Display given data as a list"""
    i=0
    print("Location: \t\t Air Quality in June: \t\t Air Quality in October:")
    while i < len(location):
        print(f"{location[i]:<15} \t\t  {june[i]:>5} \t\t {oct[i]:>10}")
        i+=1

def display_data(mean:float,median:float,good_percent:float,compared_list:list,month:str)->None:
    """Display the mean, median, percentage of good air qualities, and worst stations for each month"""
    print(f"For {month}:\n\tMean = {mean:.1f}\n\tMedian = {median:.1f}\n\tPercentage Good = {good_percent:.1f}%\n\tWorst Stations:")
    i=0
    while i < len(compared_list):
        print(f"\t\t{compared_list[i][0]} = {compared_list[i][1]}")
        i+=1

# def function_directory()->