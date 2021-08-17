matriz= []
    for i in range (0,n_i):
        matriz_c=[]
    for j in range (0,n_c):
        print(">>>> Digite o elemento [",i+1,"][",j+1,"] da matriz" ,end="")
        elemento_matriz=int(input("==> "))
        matriz_c.append(elemento_matriz)
        matriz.append(matriz_c)
        
    def escreva_matriz(matriz):
        n_l=len(matriz)
        n_c=len(matriz[0])
        for i in range (0, n_l):
            for j in range (0, n_c):
                print("\t\t",matriz[i][j], end="")
                print("")
                return

    def soma_matriz(matriz1,matriz2):
        nl_matriz1=len(matriz1)
        nl_matriz2=len(matriz2)
        if nl_matriz1 !=nl_matriz2:
            return "matrizes incompatives - numeros de colunas diferentes)-:"
        matriz_soma=[]
        linha_matriz=[]
        for i in range (0,nl_matriz1):
            for j in range (0,nc_matriz):
                linha_matriz.append(0)
                matriz_soma.append(linha_matriz)
                linha_matriz=[]
                for i in range (0,nl_matriz1):
                    for j in range (0,nc_matriz1):
                        matriz_soma[i][j]+matriz2[i][j]
                        return matriz_soma
