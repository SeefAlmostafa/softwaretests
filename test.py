ein_tupel = (1,2,3,4,"Usb","Hallo",4,"Usb","World")
print(ein_tupel)  #(1, 2, 3, 4, 'Usb', 'Hallo', 4, 'Usb', 'World')
print(ein_tupel [4:]) #('Usb', 'Hallo', 4, 'Usb', 'World')
print(ein_tupel [0]) #1
print(ein_tupel [1:4]) #(2, 3, 4)
"""
if 3 in ein_tupel:
    print("Enthalten")
else:
    print("Nicht Enthalten")
"""

""" 
for x in ein_tupel:
    print(x)
"""
noch_ein_tupel = ("Seef","Almostafa")
vereinigung = ein_tupel + noch_ein_tupel
print(vereinigung) #(1, 2, 3, 4, 'Usb', 'Hallo', 4, 'Usb', 'World', 'Seef', 'Almostafa')

#Tupel Methoden
f = ein_tupel.count("Usb")
print(f) # 2 Usb
f = ein_tupel.index(4)
print(f) # der Zahl 4 befindet sich an der stelle 3