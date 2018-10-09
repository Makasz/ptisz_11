import math
import numpy as np

k = 0
h = 0.6

number_of_instances = []
current_instace = -1
with open('sch10.txt', 'r') as file:
    for i, row in enumerate(file):
        row = ' '.join(row.replace('\n', '').split())
        if i == 0:
            number_of_instances = row.strip()
            instance = [[] for x in range(int(number_of_instances))]
            continue
        row = row.split(' ')
        if len(row) == 1:
            current_instace += 1
        if len(row) == 3:
            instance[current_instace].append(row)

print("Instance " + str(k) + ": " + str(instance[k]))
p_sum = sum([int(x[0]) for x in instance[k]])
print("Sum of p(i): " + str(p_sum))

d = p_sum * float(h)
print("d: " + str(d))
e_ordered = sorted(instance[k], key = lambda x: int(x[1]) - int(x[2])) #sorted by early - tard
# print(e_ordered)
penalty = 0 
time = 0
for i in e_ordered:
    time += int(i[0])
    if time < d:
        penalty += int(i[1])
    if tiem > d:
        penalty += int(i[2])
print("Penalty: " + str(penalty))


