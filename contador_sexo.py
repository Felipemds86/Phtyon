contador_f = 0
contador_m = 0

sexo = input(" Digite o sexo: ")
sexo = sexo.lower()
while (sexo != 'fim'):
    if (sexo == 'feminino' or sexo == 'f'):
        contador_f = contador_f +1
    elif (sexo == 'masculino' or sexo == 'm'):
        contador_m = contador_m +1
    sexo = input("Digite o sexo: ")
    sexo = sexo.lower
print("Pessoas do sexo feminino : " , contador_f)
print("Pessoas do sexo feminino : " , contador_m)

        
