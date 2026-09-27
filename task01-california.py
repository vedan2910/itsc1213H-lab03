file=open('california_housing.csv','r')
file_content=file.readlines()
def avg_median(content:list)->float:
    avg_inc=0
    list_income=[]
    for line in content[1:]:
        line=line.strip().split(',')
        med_inc=float(line[0])
        list_income.append(med_inc)
    total=0
    for value in list_income:
        total=value+total
    avg=total/len(list_income)
    return avg
avg_med_inc=avg_median(content=file_content)
print(avg_med_inc)
def high_low(content:list):
    #Finds the highest and lowest median income of houses
    list_inc=[]
    for line in content[1:]:
        line=line.strip().split(',')
        med_inc=float(line[0])
        list_inc.append(med_inc)
    high=0
    low=0
    for val in list_inc:
        if val>high:
            high=val
        if val<low:
            low=val
    return high,low
high_inc,low_inc=high_low(content=file_content)
print("Highest Median Income:",high_inc)
print('Lowest Median Income:',low_inc)
def avg_room(content:list)->float:
    #Finds avg room size of houses>600 pop
    list_room=[]
    for line in content[1:]:
        line=line.strip().split(',')
        room=float(line[2])
        population=float(line[4])
        if population>600:
            list_room.append(room)
    total=0
    for v in list_room:
        total=v+total
    avg=total/len(list_room)
    return avg
avg_room_size=avg_room(content=file_content)
print("Avg Room Size:",avg_room_size)
def avg_age(content:list)->float:
    #Finds avg age of houses w/ 1-6 bedrooms
    list_age=[]
    for line in content[1:]:
        line=line.strip().split(',')
        age=float(line[1])
        bedroom=float(line[3])
        if 1<bedroom<6:
            list_age.append(age)
    total=0
    for vals in list_age:
        total=vals+total
    a=total/len(list_age)
    return a
avg_house_age=avg_age(content=file_content)
print('Avg House Age:',avg_house_age)
def avg_occ(content:list)->float:
    #Finds avg occupancy of houses in CA based on lat/long
    list_occ=[]
    for line in content[1:]:
        line=line.strip().split(',')
        occupancy=float(line[5])
        latitude=float(line[6])
        longitude=float(line[7])
        if 34<=latitude<=37 and -122<=longitude<=-116:
            list_occ.append(occupancy)
    total=0
    for vls in list_occ:
        total=vls+total
    avg=total/len(list_occ)
    return avg
avg_occupncy=avg_occ(content=file_content)
print('Avg Occupancy:',avg_occupncy)
file.close()
