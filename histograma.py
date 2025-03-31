from math import ceil

print("---------------------------------------------")
while True:
    try:
        pesoO = float(input(" Peso da Obra: ").replace(".","").replace(",",".").strip())
        if pesoO <= 0:
            print("ERRO! Valor inválido.")
            continue
    except ValueError:
        print("ERRO! Valor inválido.")
        continue
    while True:  
        try:  
            prazoE = int(input(" Prazo de Execução (meses): "))
            if prazoE <= 0:
                print("ERRO! Valor inválido.")
                continue
            break
        except ValueError:
            print("ERRO! Valor invávalido.")
            continue  
    while True:
        try:
            taxaP = int(input(" Taxa de Produção em Kg: "))
            if taxaP <= 0:
                print("ERRO! Valor inválido.")
                continue
            break
        except ValueError:
            print("ERRO! Valor inválido")
            continue      
    print("---------------------------------------------")
    ndp = ndp = pesoO / (prazoE * taxaP * 22 * 8)
    pessoas = ceil(ndp)
    texto = "HISTOGRAMA"
    print(F"{texto:^45}")
    print("")
    print(f" PESO: {pesoO}kg")
    print(f" PRAZO: {prazoE} meses.")
    print(f" TAXA DE PRODUÇÃO: {taxaP}Kg")
    print("")
    print(f"--------------------------------------------")
    print(f" Serão nescessário {pessoas} profissionais.")
    print("---------------------------------------------")
    break