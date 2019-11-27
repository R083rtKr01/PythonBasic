# f(a,b,c)
a = False # jak zmienie na 0 i analogicznie dla dla pozostałych argumentów to otrzymam formę zero jedynkową
b = False
c = True
z1 = not a and not b and not c
z2 = not a and not b and c
z3 = not a and b and not c
z4 = a and not b and not c
# kolejna wartwa

wor = z1 or z2 or z3 or z4
print(wor)
