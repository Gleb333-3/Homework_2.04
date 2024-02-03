numbers = [
[1, 2, 3],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
['a', 'b', 'c', 'd', 'e', 'f', 'g'],
['a1', 'b2', 'c3', 'd4', 'e5', 'f6'],
['aa', 'bb', 'cc']
]
for n in numbers:
    try:
        print(n[6])
    except IndexError:
        print("This element does not exist")
