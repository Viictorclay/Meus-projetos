print("                      IDEIA 001                       ")
print("------------------------------------------------------")
print("------------------------------------------------------")
print("                ESCOLA JAVALI CANSADO                 ")
print("------------------------------------------------------")
aluno = input(" NOME DO ALUNO: ")
dinenheiro = float(input(" DINHERO: R$"))
while True:
    presenca = input(" O ALUNO FEZ TODAS AS PROVAS? ")
    if presenca == "Sim" or presenca == "sim":
        nota1 = float(input(" PRIMEIRA NOTA: "))
        nota2 = float(input(" SEGUNDA NOTA: "))
        nota3 = float(input(" TERCEIRA NOTA: "))
        media = (nota1 + nota2 + nota3) /3
        print(f" MEDIA: {media}")
        if media >= 6:
            print(" ALUNO APROVADO! ")
        elif media < 6:
             print(" ALUNO REPOVADO. ")
        else:
             print(" RESPOSTA INVALIDA, TENTE NOVAMENT. ")
              

    elif presenca == "Não" or presenca == "nao" or presenca == "não":
        fezAL = (input(" MAS CHEGOU A FZER ALGUMA ? "))
        if fezAL == "Sim" or fezAL == "sim":

            #opcoes_validas = ["prieira", "segunda", "terceira"]

            quais = input(" QUAIS PROVAS FORAM FEITAS? ")#.strip().lower()
            if quais == "primera" or quais == "Primeira":
                nota1 = float(input(" NOTA: "))
                nota2 = 0
                nota3 = 0
                media = (nota1 + nota2 + nota3) /3
                print(f" MEDIA {media} ")
                if media >= 6:
                        print(" ALUNO APROVADO! ")
                elif media < 6:
                        print(" ALUNO REPROVADO. ")
                else:
                        print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")


            elif quais == "segunda" or quais == "Segunda":
                nota1 = 0
                nota2 = float(input(" NOTA: "))
                nota3 = 0
                media = (nota1 + nota2 + nota3) /3
                print(f" MEDIA: {media}")
                if media >= 6:
                    print(" ALUNO APROVADO! ")
                elif media <= 6:
                    print(" ALUNO REPROVADO. ")
                else:
                    print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")

                
            elif quais == "Terceira" or quais == "Terceira":
                nota1 = 0
                nota2 = 0
                nota3 = float(input(" NOTA: "))
                media = (nota1 + nota2 + nota3) /3
                print(f" MEDIA: {media}")
                if media >= 6:
                    print(" ALUNO APROVADO! ")
                elif media <= 6:
                    print(" ALUNO REPROVADO. ")
                else:
                    print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")


            elif quais == "primeira" and quais == "segunda":
                nota1 = float(input(" NOTA: "))
                nota2 = float(input(" NOTA: "))
                nota3 = 0
                media = (nota1 + nota2 + nota3) /3
                print(f" MEDIA: {media}")
                if media >= 6:
                    print(" ALUNO APROVADO! ")
                elif media <= 6:
                    print(" ALUNO REPROVADO. ")        
                else:
                    print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")  


            else:
                print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")       
        else:
            print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")                 
    else:
        print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")                