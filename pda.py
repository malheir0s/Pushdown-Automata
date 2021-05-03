class Linguagem:
    def __init__(self):
        self.estados = []
        self.simbolos = []
        self.alfabetoPilha = []
        self.dicionario = dict()
        self.palavrasTeste = []
        self.estadosFinais = []
        self.pilhaTransicoes = []

    def lerTransicoes(self, num):
        for i in range (0, num):
            transicoes = input().split()
            self.criarDicionario(transicoes)

    def criarDicionario(self, transicoes):
        tripla = transicoes[0]+transicoes[1]+transicoes[2]
        if(tripla in self.dicionario):
            self.dicionario[tripla] = self.dicionario[tripla] + [[transicoes[3], transicoes[4]]]
        else:
            novaTransicao = {transicoes[0]+transicoes[1]+transicoes[2]:[[transicoes[3], transicoes[4]]]}
            self.dicionario.update(novaTransicao)

    def validarTransicao(self, estadoAtual, palavra, pilha, pilhaTransicoes):
        caractereConsumido = palavra[0:1]
        simboloTopoPilha = pilha[0:1]

        if((estadoAtual+caractereConsumido+simboloTopoPilha) in self.dicionario):
          duplas = self.dicionario.get(estadoAtual+caractereConsumido+simboloTopoPilha)
          for dupla in duplas:
            pilhaTransicoes.append([dupla[0], self.consumirSimbolo(palavra), self.empilharSimbolo(self.consumirSimbolo(pilha), dupla[1]) ])
        if( (estadoAtual+'*'+simboloTopoPilha) in self.dicionario ):
          duplas = self.dicionario.get(estadoAtual+'*'+simboloTopoPilha)
          for dupla in duplas:
            pilhaTransicoes.append([dupla[0], palavra, self.empilharSimbolo(self.consumirSimbolo(pilha), dupla[1])])
        if((estadoAtual+caractereConsumido+'*') in self.dicionario):
          duplas = self.dicionario.get(estadoAtual+caractereConsumido+'*')
          for dupla in duplas:
            pilhaTransicoes.append([dupla[0], self.consumirSimbolo(palavra), self.empilharSimbolo(pilha, dupla[1]) ])
        if((estadoAtual+'**') in self.dicionario):
          duplas = self.dicionario.get(estadoAtual+'**')
          for dupla in duplas:
            pilhaTransicoes.append([dupla[0], palavra, self.empilharSimbolo(pilha, dupla[1])])
        
    def consumirSimbolo(self, string):
        return string[1:len(string)]

    def empilharSimbolo(self, pilha, string):
      if(string == '*'):
        return pilha
      else:
        return string+pilha

    def isAccepted(self, estado, palavra, pilhaSimbolo):
      if(len(palavra)==0 and len(pilhaSimbolo)==0 and estado in self.estadosFinais):
        return True
      else:
        return False


    def percorrerPilhaTransicoes(self, palavra, estadoInicial):
        self.pilhaTransicoes = [[estadoInicial, palavra, '']]
        aceita = False
        while (not (len(self.pilhaTransicoes)==0)):
            novaPilhaTransicoes = []

            for pilha in self.pilhaTransicoes:  
              self.validarTransicao(pilha[0], pilha[1], pilha[2], novaPilhaTransicoes)
              if(self.isAccepted(pilha[0], pilha[1], pilha[2])):
                aceita = True
                break

            if(aceita):
              break
            self.pilhaTransicoes = novaPilhaTransicoes
       
        
        if(aceita):
            print('S')
        else:
            print('N')
            




L1 = Linguagem()
L1.estados = input()
L1.simbolos = input()
L1.alfabetoPilha = input()
numeroTransicoes = int(input())
L1.lerTransicoes(numeroTransicoes)
estadoInicial = input()
L1.estadosFinais = input().split()
L1.palavrasTeste = input().split()

for words in L1.palavrasTeste:
    L1.percorrerPilhaTransicoes(words, estadoInicial)


