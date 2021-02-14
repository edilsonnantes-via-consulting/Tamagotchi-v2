class bichinhoVirtual:
    def __init__ (self, nome):
        self.nome = nome
        self.fome = 20
        self.saude = 80
        self.sono = 20
        self.humor = 50
        self.idade = 1

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def alterarFome(self, valorF):
        self.fome += valorF
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0

    def alterarSaude(self, valorS):
        self.saude += valorS
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0

    def alterarSono(self, valorSo):
        self.sono += valorSo
        if self.sono > 100:
            self.sono = 100
        elif self.sono < 0:
            self.sono = 0

    def alterarHumor(self, valorH):
        self.humor += valorH
        if self.humor > 100:
            self.humor = 100
        elif self.humor < 0:
            self.humor = 0

    def alterarIdade(self):
        self.idade += 1

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarSono(self):
        return self.sono

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        return self.humor


nomeB = input('Qual será o nome do seu mascote? ')
bichinho = bichinhoVirtual(nome = nomeB)

while (bichinho.saude > 0) and (bichinho.fome < 100) and (bichinho.sono < 100) and (bichinho.humor > 0):
    
    bichinho.alterarFome(+2)
    bichinho.alterarSaude(-2)
    bichinho.alterarSono(+2)
    if (bichinho.retornarSaude() < 40) or (bichinho.retornarFome() > 60) or (bichinho.retornarSono() > 60):
        bichinho.alterarHumor(-5)
    elif (bichinho.retornarSaude() < 40) and (bichinho.retornarFome() > 60) and (bichinho.retornarSono() > 60):
        bichinho.alterarHumor(-20)
    else:
        bichinho.alterarHumor(-2)
    bichinho.alterarIdade()
    
    resposta = input(f"""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
     \nOlá meu nome é {bichinho.nome}. O que vamos fazer agora? \n1- Alimentar (-10 de fome)\n2- Dar remédio (+10 de saúde)\n3- Dormir (-10 de sono)\n4- Brincar (+10 de humor)\n5- Alterar nome\n6- Visualizar humor\n7- Visualizar idade\n8- Visualizar fome\n9- Visualizar saúde\nResposta: """)
    print('\n')

    if resposta == '1':
        bichinho.alterarFome(-10)
        print('-10 de fome! Obrigado!')
    elif resposta == '2':
        bichinho.alterarSaude(+10)
        print('+10 de saúde! Obrigado!')
    elif resposta == '3':
        bichinho.alterarSono(-10)
        print('-10 de sono! Obrigado!')
    elif resposta == '4':
        bichinho.alterarHumor(+10)
        print('+10 de humor! Obrigado!')
    elif resposta == '5':
        nome2 = input('Qual nome deseja colocar? \n')
        bichinho.alterarNome(nome2)
    elif resposta == '6':
        print('Humor: ', bichinho.retornarHumor())
    elif resposta == '7':
        print("Idade: ", bichinho.retornarIdade(), " dias")
    elif resposta == '8':
        print('Fome: ', bichinho.retornarFome())
    elif resposta == '9':
        print('Saúde: ', bichinho.retornarSaude())
    else:
        print('Escolha um número válido!')

else:
    print("""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\nVocê deixou seu mascote morrer!\n""")