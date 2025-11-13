def mean_calc(air_data:list)->int:
    """Find the mean from a list of air quality data"""
    i = 0
    sum = 0
    while i < len(air_data):
        sum+=air_data[i]
        i+=1
    sum = sum//len(air_data)
    # print(sum)
    return sum
    
def median_calc(air_data:list)->int:
    """Find the median from a list of air quality data"""
    # print(air_data)
    # print(len(air_data))
    if (len(air_data)%2)==0:
        middle = (air_data[len(air_data)//2] + air_data[(len(air_data)//2)-1])//2
        print(air_data[len(air_data)//2], air_data[(len(air_data)//2)+1])
    else:
        middle = air_data[((len(air_data)+1)//2)]
        print(((len(air_data)+1)//2))
    return middle

def assign_air_quality(location_data:list, month:str)->list:
    """Assign air qaulity data to location names"""
    i = 0
    air_data = []
    location_air_data = []
    data_compiled = []
    while i<len(location_data):
        data_month = int(input(f"{location_data[i][0]}'s air quality in {month} "))
        air_data.append(data_month)
        location_air_data.append([location_data[i][0], data_month])
        i+=1
        data_compiled.append(location_air_data)
        data_compiled.append(air_data)
    return data_compiled

def compare_air_quality(location_data:list, sorted_data:list)->list:
    """Return a list of the locations with the worst air quality"""
    print(location_data)
    print(sorted_data)

    sorted = []
    i=0
    while i<len(location_data):
        # print("hi hello")
        j=2 
        while j >= 1:
            # print("hello")
            if location_data[i][1]==sorted_data[-1*j] and not location_data[i][0] in sorted:
                # print("hi")
                sorted.append(location_data[i][0])
            j-=1
            
        i+=1
        # if 
    print(sorted)
    return sorted

def find_percent(num_list:list,comparison:int)->float:
    """Return the percentage of items that are above a specified value"""
    greater_than = []
    i = 0
    while i < len(num_list):
        if num_list[i] >= comparison:
            greater_than.append(num_list[i])
        i+=1
    percent = (len(greater_than)/len(num_list))*100
    return percent

# def function_directory()->