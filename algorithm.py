# 
# Owen Morgan
# Oct. 22
# 
# 
# 

def main()->None:
    list = []
    location = input("Location (\"END to stop\"): ")
    while location != "END":
        sub_list = []
        sub_list.append(location)
        data_june = int(input("Air quality in June: "))
        data_oct = int(input("Air quality in October: "))
        sub_list.append(data_june)
        sub_list.append(data_oct)
        list.append(sub_list)
        location = input("Location (\"END to stop\"): ")
    i = 0
    while i <len(list):
        print(f"{i+1}. {list[i][0]} {list[i][1]} {list[i][2]}")
        i+=1
    
main()