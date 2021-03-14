from itertools import cycle

my_list = ['щука', 'съела', 'ацетат']
i = 0
for el in cycle(my_list):
    if i > 8:
        break
    print(el)
    i += 1
