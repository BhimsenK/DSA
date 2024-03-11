list1 = [12, 'shree', 'rh', 111]
for i in list1:
    if isinstance(i, int):
        list1.remove(i)

print(list1)
