tabla = [[0 for x in range(15)] for y in range(5)]
for i in range(5):
    for j in range(15):
        if i == 0 or i == 4 or j == 0 or j == 14:
            tabla[i][j] = 1          
print("\n".join(str(x) for x in tabla))
print()