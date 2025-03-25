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
        nota1 = float(input(" NOTA DA PRIMEIRA PROVA: "))
        nota2 = float(input(" NOTA DA SEGUNDA PROVA: "))
        nota3 = float(input(" NOTA DA TERCEIRA PROVA: "))
        media = (nota1 + nota2 + nota3) /3
        print(f" MEDIA: {media}")
        if media >= 6:
            print(" ALUNO APROVADO! ")
            break
        elif media < 6:
             print(" ALUNO REPOVADO. ")
             break
        else:
             print(" RESPOSTA INVALIDA, TENTE NOVAMENT. ")

    elif presenca == "Não" or presenca == "nao" or presenca == "não":
        fezAL = (input(" MAS CHEGOU A FZER ALGUMA ? "))
        if fezAL == "Sim" or fezAL == "sim":

            opcoes_validas = ["prieira", "segunda", "terceira"]

            quais = input(" QUAIS PROVAS FORAM FEITAS? ").strip().lower()
            if quais == "primeira":
                nota1 = float(input(" NOTA DA PRIMEIRA PROVA: "))
                nota2 = 0 ; print(" NOTA DA SEGUNDA PROVA: -")
                nota3 = 0 ; print(" NOTA DA TERCEIRA PROVA: -")
                media = (nota1 + nota2 + nota3) /3
                print(f" MEDIA {media:.1f} ")
                if media >= 6:
                    print(" ALUNO APROVADO! ")
                    break
                elif media < 6:
                    print(" ALUNO EM RECUPERAÇÃO. ")
                    break
                else:
                    print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")
                    

            elif quais == "segunda":
                nota1 = 0 ; print(" NOTA DA PRIMEIRA PROVA: -")
                nota2 = float(input(" NOTA DA SEGUNDA PROVA: "))
                nota3 = 0 ; print(" NOTA DA TERCEIRA PROVA: -")
                media = (nota1 + nota2 + nota3) /3
                print(f" MEDIA: {media:.1f}")
                if media >= 6:
                    print(" ALUNO APROVADO! ")
                    break
                elif media < 6:
                    print(" ALUNO EM RECUPERAÇÃO. ")
                    break
                else:
                    print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")

            elif quais == "terceira":
                nota1 = 0 ; print(" NOTA DA PRIMEIRA PROVA: ")
                nota2 = 0 ; print(" NOTA DA SEGUNDA PROVA: ")
                nota3 = float(input(" NOTA: "))
                media = (nota1 + nota2 + nota3) /3
                print(f" MEDIA: {media:.1f}")
                if media >= 6:
                    print(" ALUNO APROVADO! ")
                    break
                elif media < 6:
                    print(" ALUNO EM RECUPERAÇÃO. ")
                    break
                else:
                    print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")

            elif "primeira" in quais and "segunda" in quais:
                nota1 = float(input(" NOTA DA PRIMEIRA PROVA: "))
                nota2 = float(input(" NOTA DA SEGUNDA PROVA: "))
                nota3 = 0 ; print(" NOTA DA TERCEIRA PROVA: -")
                media = (nota1 + nota2 + nota3) /3
                print(f" MEDIA: {media:.1f}")
                if media >= 6:
                    print(" ALUNO APROVADO! ")
                    break
                elif media < 6:
                    print(" ALUNO EM RECUPERAÇÃO. ")
                    break       
                else:
                    print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")  

            elif "primeira" in quais and "terceira" in quais:
                nota1 = float(input(" NOTA DA PRIMEIRA PROVA: "))
                nota2 = 0 ; print(" NOTA DA SEGUNDA PROVA: -")
                nota3 = float(input(" NOTA DA TERCEIRA PROVA: "))
                media = (nota1 + nota2 + nota3) /3
                print(f"MEDIA: {media:.1f}")
                if media >= 6:
                    print(" ALUNO APROVADO! ")
                    break
                elif media < 6:
                    print(" ALUNO EM RECUPERÇÃO. ")
                    break    
                else:
                    print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")

            elif "segunda" in quais and "terceira" in quais:
                nota1 = 0 ; print(" NOTA DA PRIMEIRA PROVA: -")
                nota2 = float(input(" NOTA DA SEGUNDA PROVA: "))
                nota3 = float(input(" NOTA DA TERCEIRA PROVA: "))
                media = (nota1 + nota2 + nota3) /3
                print(f" MEDIA: {media:.1f}")
            
                if media >= 6:
                    print(" ALUNO APROVADO! ")
                    break
                elif media < 6:
                    print(" ALUNO EM RECUPERAÇÃO. ")
                    break
                else:
                    print(" RESPOSTA INVALIDA, TENTE NOVAMENTE. ")
            else:
                print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")
        #FAZER ALGO COM DINEHRO AQUI        

        elif fezAL == "não" or fezAL == "Não" or fezAL == "nao":
            print(" ALUNO REPROVADO. ")
            break
        else:
            print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")
    else:
        print(" RESPOSTA INVALIDA, TENTE NOVAMENTE.")
