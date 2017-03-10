class Fila:
    def __init__(self):
        self.Input = None
        self.Output = None
    def inserir(self,dado):
        novoNo = No(dado)
        if self.Output is None:
            self.Output = novoNo
            self.Input = novoNo
        self.Input.referenciaNo = novoNo
        self.Input = novoNo
    def remover(self):
        tempNo = self.Output
        self.Output = self.Output.referenciaNo
        tempNo.referenciaNo = None
        return tempNo.dado
    #def emtpty(self):

class No:
    def __init__(self, dado):
        self.dado = dado
        self.referenciaNo = None