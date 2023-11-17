rating = {}

flavors = []
f = open("flavors.txt", "r")
line = f.readline().strip().lower()
flavors.append(line)

for line in f:
    x = line.strip().lower()
    flavors.append(x)

lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
for i in range(len(flavors)):
    if "cookie" in flavors[i] and "chocolate" in flavors[i]:
        lst1.append(flavors[i])
        rating[1] = lst1
    elif "cookie" in flavors[i]:
        lst2.append(flavors[i])
        rating[2] = lst2
    elif "chocolate" in flavors[i]:
        lst3.append(flavors[i])
        rating[3] = lst3
    elif " " not in flavors[i]:
        lst4.append(flavors[i])
        rating[4] = lst4
    else:
        lst5.append(flavors[i])
        rating[5] = lst5

for i in range(5):
    val = str(rating[i + 1])
    val = val[1:len(val) - 1]

    print(str(i + 1) + ":", val)
