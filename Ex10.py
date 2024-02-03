students = [ ("Aiana", 22, 80), ("Iskhak", 26, 60), ("Maria", 23, 85), ("Alexey", 21, 70) ]

new_dictionary = {name:{"age:": age, "average:": avg } for name, age, avg in students if age < 25 and avg > 75}
print(new_dictionary)