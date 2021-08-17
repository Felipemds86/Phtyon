# calculo hipotenusa 


def hipotenusa (cat_a, cat_b):
    import math
    h=math.sqrt(math.pow(cat_a,2)+math.pow(cat_b,2))
    return h


a=float(input("Digite o valor do primeiro cateto , a ==>"))
b=float(input("Digite o valor do segundo cateto , b ==>"))
hip = hipotenusa( a,b)
print ("hipotenusa = ", hip)
