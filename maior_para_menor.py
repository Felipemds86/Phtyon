# programa para verificar o numero maior entre tres numeros em ordem crescente.



a=int(input("Digite o primeiro numero:"))
b=int(input("Digite o segundo  numero:"))
c=int(input("Digite o terceiro numero:"))

if a>=b:
    if c>=a:
        print("\t menor= ", b,"\t medio = ", a , "\t maior = ", c)
    else:
        if c > b:
            print("\t menor= ", b,"\t medio = ", c , "\t maior = ", a)
        else:
                print("\t menor= ", c,"\t medio = ", b , "\t maior = ", a)
                
else:
    if c >= b:
        print("\t menor= ", a,"\t medio = ", b , "\t maior = ", c)
    else:
       if c >=a:
         print("\t menor= ", a,"\t medio = ", c , "\t maior = ", b)
       else:
         print("\t menor= ", c,"\t medio = ", a , "\t maior = ", b)
        
