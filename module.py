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

def assign_air_quality(location_data:list)->list:
    """Assign air qaulity data to location names"""
    i = 0
    air_data_compiled = []
    while i<len(location_data):
        data_oct = int(input(f"{location_data[i][0]}'s air quality in October: "))
        air_data_compiled.append(data_oct)
        i+=1
    return air_data_compiled

def compare_air_quality(air_data:list, location_data:list)->list:
    sorted = []
    sorted.append(location_data[air_data[0]])
    sorted.append(location_data[air_data[len(air_data)-1]])
    return sorted