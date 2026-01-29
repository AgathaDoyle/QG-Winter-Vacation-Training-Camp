text=" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X"
new_text=text.split(";")
dict={}
for i in new_text:
    new_i=i.strip().split(":")
    if new_i[0]=="Agent":
        dict[new_i[0]]=new_i[1]
    elif new_i[0]=="Mission":
        dict[new_i[0]]=new_i[1]
        core_mission=i.strip()[len("Mission:"):]
    elif new_i[0]=="Items":
        dict[new_i[0]]=list(set(new_i[1].split(",")))
    else:
        str = new_i[1].strip("()")
        part = str.split(",")
        x = int(part[0])
        y = int(part[1])
        dict[new_i[0]] = (x, y)
print(dict)
print(core_mission)






