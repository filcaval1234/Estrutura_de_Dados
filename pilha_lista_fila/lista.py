class lista:
    def __init__(self):
        self.referencia = None

    def insertNo(self, dado):
        no = No(dado)
        no.referenciaNo = self.referencia
        self.referencia = no

    def pop(self):
        if self.referencia is None:
            return "vazia"
        tempNo = self.referencia
        self.referencia = tempNo.referenciaNo
        return tempNo.dado

    def InsertOrdenado(self, valor):
        novoNo = No(valor)
        if self.referencia is None:
            self.referencia = No(valor)
        elif self.referencia.dado > valor:
            novoNo.referenciaNo = self.referencia
            self.referencia = novoNo
        else:
            tempNo = self.referencia
            noAnterior = None
            while tempNo != None and valor > tempNo.dado:
                noAnterior = tempNo
                tempNo = tempNo.referenciaNo
            if noAnterior is not None:
                novoNo.referenciaNo = tempNo
                noAnterior.referenciaNo = novoNo
            else:
                novoNo.referenciaNo = self.referencia
                self.referencia = novoNo

    def Lista_Ate_Num(self,dado = None):
        TempList = lista()
        TempNo = self.referencia
        while TempNo.dado is not dado:
            TempNo = TempNo.referenciaNo
            if TempNo == None:
                return ValueError
        while TempNo is not None:
            TempList.InsertOrdenado(TempNo.dado)
            TempNo = TempNo.referenciaNo
        return TempList

    def Push_Repeat_Ord(self):
        NoAtual = self.referencia
        NoPassado = None
        while NoAtual is not None:
            if NoPassado is not None:
                while NoAtual.dado == NoPassado.dado:
                    NoPassado.referenciaNo = NoAtual.referenciaNo
                    NoAtual.referenciaNo = None
                    NoAtual = NoPassado.referenciaNo
                if NoAtual is None:
                    break
            NoPassado = NoAtual
            NoAtual = NoAtual.referenciaNo

    def Push_Repeat_Noord(self):
        tempList = lista()
        tempNo1 = self.referencia
        while tempNo1 is not None:
            if tempList.returnPosicaoDado(tempNo1.dado) == -1:
                tempList.InsertOrdenado(tempNo1.dado)
            tempNo1 = tempNo1.referenciaNo
        return tempList
                
        
    def returnPosicaoDado(self, dado):
        pos = -1
        if self.referencia is None:
            return -1
        tempNo = self.referencia
        while tempNo is not None:
            pos +=1
            if tempNo.dado is dado:
                return pos
            tempNo = tempNo.referenciaNo
        return -1

    def copia(self):
        tempList = lista()
        if self.referencia is None:
            return None
        tempNo = self.referencia
        while tempNo is not None:
            tempList.insertNo(tempNo.dado)
            tempNo = tempNo.referenciaNo
        return  tempList

    def concatena(self, l1, l2):
        l11 = l1.copia()
        l22 = l2.copia()
        tempNo = l11.referencia
        while tempNo.referenciaNo is not None:
            tempNo = tempNo.referenciaNo
        tempNo.referenciaNo = l22.referencia
        return  l11

    def intercalados(self, lista1, lista2):
        tempNo1 = lista1.referencia
        tempNo2 = lista2.referencia
        tempList = lista()
        while tempNo1 is not None or tempNo2 is not None:
            if tempNo1 is not None:
                tempList.insertNo(tempNo1.dado)
                tempNo1 = tempNo1.referenciaNo
            if tempNo2 is not None:
                tempList.insertNo(tempNo2.dado)
                tempNo2 = tempNo2.referenciaNo

        return tempList
        
    #vai retornar o número de elementos pares a soma dos valores da lista e todos os numeros primos da lista
    def Quant(self):
        cont_aux = 0
        cont = 0
        soma = 0
        lista_primos = []
        TempNo = self.referencia
        while TempNo is not None:
            if TempNo.dado % 2 == 0:
                cont +=1
            soma += TempNo.dado
            for i in range(2, TempNo.dado):
                if TempNo.dado % i != 0:
                    cont_aux += 0
                if TempNo.dado % i ==0:
                    cont_aux+=1
            if cont_aux == 0:
                lista_primos.append(TempNo.dado)
            cont_aux = 0
            TempNo = TempNo.referenciaNo
        return {'Num_par': cont, 'Sum_Num': soma,'List_primos': lista_primos}


    def insertlist(self):
        TempNo = self.referencia
        templist = lista()
        while TempNo is not None:
            templist.InsertOrdenado(TempNo.dado)
            TempNo = TempNo.referenciaNo
        return templist

    def listpar(self):
        if self.referencia is None:
            return None
        cont = 0
        ListaTemp = lista()
        NoAtual = self.referencia
        while NoAtual != None:
            if cont % 2 == 0:
                ListaTemp.InsertOrdenado(NoAtual.dado)
            cont +=1
            NoAtual = NoAtual.referenciaNo
        return  ListaTemp





class No:
    def __init__(self, dado):
        self.dado = dado
        self.referenciaNo = None
