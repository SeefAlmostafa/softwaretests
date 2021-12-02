#Taschenrechner by Seef und Mohammed

def sum(x,y):return x+y
def sub(x,y):return x-y
def mal(x,y):return x*y
def div(x,y):
    if y == 0:
        return None
    else :
        return x/y

def mod(x,y):return x%y


# Testing

x=12
y=12

print(sum(x,y))
print(sub(x,y))
print(mal(x,y))
print(div(x,y))
print(mod(x,y))