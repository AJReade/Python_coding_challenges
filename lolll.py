total_score = 5
dict1 = {}
dict1.update({"hello": 5})
print(dict1)
#temp = list(dict1.items)
#print(temp)
temp1 = []
for key, val in dict1.items(): 
    temp1.append([key] + [val]) 
print(temp1)