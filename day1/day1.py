with open('input.txt') as f:
    lines = f.readlines()

first_list = list()
second_list = list()
count = 0

for line in lines:
    first_list.append(line[0:6])
    second_list.append(line[7:13])

ordered_first = sorted(first_list)
ordered_second = sorted(second_list)

total_diff = 0

for f,s in zip(ordered_first, ordered_second):
    total_diff = total_diff + abs(int(f)-int(s))

#test change 2
    
print(total_diff)
               
            
