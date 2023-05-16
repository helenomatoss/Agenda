compromisso1 = {
	"dia-da-semana" : "Sabado",
	"horario" : 9,
	"texto": "Igreja."
}
compromisso2 = {
	"dia-da-semana" : "Sabado",
	"horario" : 14,
	"texto": "Almoço na casa da vó."
}
compromisso3 = {
	"dia-da-semana" : "Domingo",
	"horario" : 20,
	"texto": "Filme."
}
agenda = [compromisso1,compromisso2,compromisso3]

def inserirNaAgenda():
    novocompromisso = {
        "dia-da-semana" : input("Digite o dia da semana do seu novo compromisso: "),
	"horario" : int(input("Digite o horário do seu novo compromisso: ")),
	"texto": input("Digite uma breve descrição do seu novo compromisso: ")
    }
    agenda.append(novocompromisso)

def checarHorarioNaAgenda(buscarAgenda):
    buscarHorario = int(input("Digite um horário a ser verificado na agenda: "))
    for umaChave in buscarAgenda:
        if(umaChave["horario"]==buscarHorario):
            print("Compromisso encontrado ás,",buscarHorario,"h",umaChave)

def substituirTextoNaAgenda(buscarAgenda):
    buscarHorario = int(input("Digite um horário a ser verificado na agenda: "))
    for umaChave in buscarAgenda:
        if(umaChave["horario"]==buscarHorario):
            print("Compromisso encontrado ás,",buscarHorario,"h",umaChave)
            substiuirtexto = input("Digite o novo texto a ser atribuido/substituido no compromisso: ")
            umaChave["texto"]=substiuirtexto
            print("Novo texto atribuido: ",umaChave["texto"],"\nCompromisso ás,",buscarHorario,"h",umaChave)

def checarCompromissosNaAgenda():
    for umaChave in agenda:
        print(umaChave)

while True:
    print()
    print("---------------------------- menu --------------------------------------")
    print("1. Inserir um novo compromisso na agenda. \n2. Pesquisar compromissos na agenda com base em um horário. \n3. Alterar/Substituir o texto de um compromisso na agenda. \n4. Exibir todos os compromissos da agenda. \n5. Fechar menu.")
    print("------------------------------------------------------------------------")
    menu = int(input("Digite um número correspondente a uma opção do menu: "))

    if(menu==1):
        inserirNaAgenda()
    elif(menu==2):
        checarHorarioNaAgenda(agenda)
    elif(menu==3):
        substituirTextoNaAgenda(agenda)
    elif(menu==4):
        checarCompromissosNaAgenda()
    elif(menu==5):
        quit()
    else:
       print("Opção inválida.")