dividable_by5 = []
for x in range(0,101):
    if x%5==0:
        dividable_by5.append(x)
cubes = [i**3 for i in dividable_by5]
print(f"Liczby z zakresu 0-100 podzielne przez 5 to: {dividable_by5}" + '\r\n' + f"Sześciany liczb z zakresu 0-100 podzielnych przez 5 to: {cubes}")