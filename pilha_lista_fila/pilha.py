from lista import *
class pilha:
    def __init__ (self):
        self.referencia = None
    def push(self,dado):
        novoNo = No(dado)
        novoNo.referenciaNo = self.referencia
        self.referencia = novoNo
    def pop(self):
        if self.empty():
            return None
        tempNo = self.referencia
        self.referencia = tempNo.referenciaNo
        tempNo.referenciaNo = None
        return tempNo.dado
    def empty(self):
        if self.referencia is None:
            return True
        return False
    def ordena_pilha(self):
        tempList = lista()
        while self.empty() is not True:
            tempList.InsertOrdenado(self.pop())
        tempNo = tempList.referencia
        while tempNo is not None:
            self.push(tempNo.dado)
            tempNo = tempNo.referenciaNo
    def removerElem(self, dado):
        pilha_aux = pilha()
        recebe_pop = None
        if self.empty():
            return "Vazia"
        while recebe_pop is not dado and self.empty() is not True:
            recebe_pop = self.pop()
            if recebe_pop is not dado:
                pilha_aux.push(recebe_pop)
        while pilha_aux.empty() is not True:
            self.push(pilha_aux.pop())


class No:
    def __init__(self, dado):
        self.dado = dado
        self.referenciaNo = None