file=open('coromon_dataset.csv','r')
file_content=file.readlines()
import random
def most_cumul(content:list)->str:
    #Finds coromon type with most health points
    health_type={}
    for line in content[1:]:
        line=line.strip().split(',')
        coromon_typ=line[1]
        cum_heal=int(line[3])
        if coromon_typ not in health_type:
            health_type[coromon_typ]=cum_heal
        else:
            health_type[coromon_typ]+=cum_heal
    highest_type=''
    highest_heal=0
    for coromon_typ in health_type.keys():
        if health_type[coromon_typ]>highest_heal:
            highest_heal=health_type[coromon_typ]
            highest_type=coromon_typ
    return highest_type
type_highest=most_cumul(content=file_content)
print('Most cumulative coromon type:',type_highest)
def most_def(content:list)->str:
    #Finds coromon with most defense points
    defense_points={}
    for line in content[1:]:
        line=line.strip().split(',')
        coromon=line[0]
        def_points=int(line[5])
        if coromon not in defense_points:
            defense_points[coromon]=def_points
        else:
            defense_points[coromon]+=def_points
    highest_coromon=''
    highest_def=0
    for coromon in defense_points.keys():
        if defense_points[coromon]>highest_def:
            highest_def=defense_points[coromon]
            highest_coromon=coromon
    return highest_coromon
corr=most_def(content=file_content)
print('Coromon w/ most def points:',corr)
def random_coromon_typ(content:list,coromon_type:str)->str:
    #Finds random coromon type based on user selection
    coromons=[]
    for line in content[1:]:
        line=line.strip().split(',')
        coromon=line[0]
        user_coromon_typ=line[1]
        if user_coromon_typ.upper()==coromon_type.upper():
            coromons.append(coromon)
    return random.choice(coromons)
coro=random_coromon_typ(content=file_content,coromon_type='ice')
print(coro)
def coromon_user(content:list,coromon_type:str)->str:
    #Finds all coromons based on user selection
    coros=[]
    for line in content[1:]:
        line=line.strip().split(',')
        coromon=line[0]
        user_coro_typ=line[1]
        if user_coro_typ.upper()==coromon_type.upper():
            coros.append(coromon)
    return coros
corr=coromon_user(content=file_content,coromon_type='fire')
print(corr)
def random_coromon(content:list)->str:
    #Finds random coromon type based on user selection
    corrs=[]
    for line in content[1:]:
        line=line.strip().split(',')
        coromon=line[0]
        corrs.append(coromon)
    return random.choice(corrs)
coro=random_coromon(content=file_content)
print(coro)
file.close()
