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
