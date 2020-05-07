import json
data = None
with open("schedule.json","r") as fin:
    data = json.load(fin)

slots = {}
for room in data:
    table = data[room]
    for x in range(5):
        for y in range(5):
            if table[x][y] == "":
                continue
            if table[x][y] not in slots.keys():
                slots[table[x][y]]=[]
            temp = str((x*10+y)) if x>0 else "0"+str(y)
            slots[table[x][y]].append(temp)

with open("slots.json","w") as fout:
    json.dump(slots, fout, indent=4) 