with open('input.txt') as f:
    lines = f.readlines()

first_list = list()
second_list = list()
count = 0

for line in lines:
    first_list.append(int(line[0:5]))
    second_list.append(int(line[8:13]))


#ordered_first = sorted(first_list)
#ordered_second = sorted(second_list)

similarity = 0

for item in first_list:
    similarity = similarity + (second_list.count(item)*item)

print(similarity)

