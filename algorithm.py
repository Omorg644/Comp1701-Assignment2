# 
# Owen Morgan
# Oct. 22
# 
# 
# 
def mean_calc(air_data:list)->float:
    i = 0
    sum = 0
    while i < len(air_data):
        sum+=air_data[i][1]
        i+=1
    # print(sum)
    return sum
    

def main()->None:
    air_data = []
    location = input("Location (\"END to stop\"): ")
    while location != "END":
        sub_list = []
        sub_list.append(location)
        data_june = int(input("Air quality in June: "))
        data_oct = int(input("Air quality in October: "))
        sub_list.append(data_june)
        sub_list.append(data_oct)
        air_data.append(sub_list)
        location = input("Location (\"END to stop\"): ")
    i = 0
    while i <len(air_data):
        print(f"{i+1}. {air_data[i][0]} {air_data[i][1]} {air_data[i][2]}")
        i+=1
    mean = mean_calc(air_data)
    print(mean)
    
main()