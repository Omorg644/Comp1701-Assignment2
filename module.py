def mean_calc(air_data:list)->int:
    """Find the mean from a list of air air quality"""
    i = 0
    sum = 0
    while i < len(air_data):
        sum+=air_data[i][1]
        i+=1
    sum = sum//len(air_data)
    # print(sum)
    return sum
    
def median_calc(air_data:list)->int:
    """Find the median from a list of air air quality"""
    middle = [air_data[len(air_data)//2][1],air_data[len(air_data)//2][2]]
    # middle.append(air_data[len(air_data)//2][2])
    return middle

def assign_air_quality(location_data:list)->list:
    """Assign air qaulity data to location names"""
    i = 0
    while i<len(location_data):
        # location_data[i]
        data_june = int(input(f"{location_data[i][0]}'s air quality in June: "))
        data_oct = int(input(f"{location_data[i][0]}'s air quality in October: "))
        location_data[i].append(data_june)
        location_data[i].append(data_oct)
        i+=1
    return location_data

def compare_air_quality(compiled_data:list)->list:
    # worst_locations = []
    check = True
    i = 0
    while check == True:
        # if i<len(compiled_data)-1:
        if i == len(compiled_data)-1:
            i=0
        if compiled_data[i][2] >= compiled_data[i+1][2]:
            smaller = (compiled_data[i+1])
            compiled_data[i+1]=compiled_data[i]
            compiled_data[i]=smaller
        else:
            check = False
        # elif compiled_data[i][2] == compiled_data[i+1][2]:
        i+=1
    print(compiled_data)
    return compiled_data