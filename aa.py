import enum
 
# creating enumerations using class
class Animal(enum.Enum):
    cão = 1
    gato = 2
    leão = 3
 
# Comparison using "is"
if Animal.cão is Animal.gato:
    print("Cão e gato são os mesmos animais")
else:
    print("Cão e gato são animais diferentes")
 
# Comparison using "!="
if Animal.leão != Animal.gato:
    print("Leões e gatos são diferentes")
else:
    print("Leões e gatos são iguais")