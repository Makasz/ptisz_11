import math

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

d = round(p_sum * float(h))
print("d: " + str(d))
# We calculate difference in penalty for earliness and tardiness (b(i) - a(i)) and take first tasks with least value.
e_ordered = sorted(instance[k], key = lambda x: int(x[1]) - int(x[2])) # Sorted tasks (accordingly to above formula)
# print(e_ordered)
penalty = 0
current_time = 0
# Penatly is calculated: abs(current_time - time_task_finished) * a(i)) if current_time < d
#                    or: abs(current_time - time_task_finished) * b(i)) if current_time > d
for i in e_ordered:
    current_time += int(i[0])
    print("Current time: {}  p(i): {} a(i): {}  b(i): {}".format(current_time, i[0], i[1], i[2]))
    if current_time < d:
        penalty += int(i[1]) * abs(current_time - d)
    if current_time > d:
        penalty += int(i[2]) * abs(current_time - d)
print("Penalty: " + str(penalty))


