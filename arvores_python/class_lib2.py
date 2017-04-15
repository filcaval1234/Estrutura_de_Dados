class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, root = -1):
        if root == -1:
            self.root = self.insert(data, self.root)
            return
        if root is None:
            root = TreeNode(data)
        elif data < root.data:
            root.left = self.insert(data, root.left)
        elif data > root.data:
            root.right = self.insert(data, root.right)
        return root

    def obterAlturaRelativa(self, altura, root = -1):
        if root == -1:
            return  self.obterAltura(altura, self.root)
        if root is not None:
            altura =  self.obterAltura(altura+1, root.left)
        return altura

    def print(self, root = -1):
        if root == -1:
            root = self.root
        if root is not None:
            self.print(root.left)
            print(root.data)
            self.print(root.right)


    def quantTree(self,quant = 0, root = -1):
        if root == -1:
            root = self.root
        if root is not None:
            return 1 + self.quantTree(quant+1, root.left) + self.quantTree(quant+1, root.right)
        return 0

    def NoPai(self,dado, root = -1):
        if root == -1 :
            no = self.NoPai(dado, self.root)
            return no

        if root is not None:
            if root.left is not None:
                if root.left.data is dado:
                    print(root.data)
            if root.right is not None:
                if root.right.data is dado:
                    print(root.data)
            self.NoPai(dado, root.left)
            self.NoPai(dado, root.right)

    def NoPai2(self,dado, root = -1):
        if root == -1 :
            root = self.root
        if root is not None:
            if root.left is not None:
                if root.left.data is  dado:
                    return  root.data
            if root.right is not None:
                if root.right.data is dado:
                    return root.data
            noe = self.NoPai2(dado, root.left)
            nod = self.NoPai2(dado, root.right)
            if noe is not None:
                return noe
            elif nod is not None:
                return nod

    def alturaTree(self, root = -1, altura = 0):
        if root == -1:
            return self.alturaTree(self.root)
        if root is not None:
            alt_esq = self.alturaTree(root.left, altura+1)
            alt_dir = self.alturaTree(root.right,altura+1)
            if alt_esq > alt_dir:
                return alt_esq
            else: return alt_dir
        return altura


    def menorValor(self, root = -1):
        if root == -1:
            return self.menorValor(self.root)
        if root.left is not None:
            return self.menorValor(root.left)
        else:
            return root.data

    def maiorValor(self, root = -1,):
        if root == -1:
            return self.maiorValor(self.root)
        if root.right is not None:
            return self.maiorValor(root.right)
        else:
            return root.data

    def quantNofolhas(self, root = -1, noFolha = 0):
        if root == -1:
            return self.quantNofolhas(self.root)
        if root is not None:
            if root.left is None and root.right is None:
                return noFolha+1
            return self.quantNofolhas(root.left, noFolha) + self.quantNofolhas(root.right, noFolha)
        return 0

    def search(self, dado, root = -1):
        if root == -1:
            return self.search(dado, self.root)
        if root is not None:
            if dado == root.data:
                return True
            esqu = self.search(dado, root.left)
            dire = self.search(dado, root.right)
            if esqu is not None:
                return esqu
            elif dire is not None: return dire

    def sum(self, root = -1, soma = 0):
        if root == -1:
            return self.sum(self.root)
        if root is not None:return root.data+self.sum(root.left, root.data)+self.sum(root.right, root.data)
        return 0

    def perfect(self):
        if 2**self.alturaTree()-1 == self.quantTree():
            return "Is perfect"

    def doubleSon(self, root = -1):
        if root == -1:return self.doubleSon(self.root)
        if root is not None:
            if (root.left is None and root.right is None):
                return 1 + self.doubleSon(root.left)
            elif (root.left is not None and root.right is not None):
                return 1 + self.doubleSon(root.right)
        return -1

    def FullTree(self):
        if self.doubleSon() + self.quantNofolhas() == self.quantTree():
            return "Is Tree Full"

    def completTree(self, root = -1, complet = None):
        if root == -1:
            return self.completTree(self.root)
        if root is not None:
            if root.left is None and root.right is not None:
                print("tafuncionando")
            else:
                esq = self.completTree(root.left)
                dir = self.completTree(root.right)

    def comparaArvore(self, arvore1, arvore2):
        if arvore1 is not None and arvore2 is not None:
            if arvore1.data != arvore2.data:
                return False
            if self.comparaArvore(arvore1.left, arvore2.left) is False or self.comparaArvore(arvore1.right, arvore2.right) is False:
                return False
            else: return True
        elif arvore1 is not  None or arvore2 is not None:
            return False

    def qtdNosIguaisAvores(self, arvore1, arvore2):
        if arvore1 is not None and arvore2 is not None:
            print(arvore1.data, arvore2.data)
            if arvore1.data == arvore2.data:
                esq = self.qtdNosIguaisAvores(arvore1.left, arvore2.left)
                dir = self.qtdNosIguaisAvores(arvore1.right, arvore2.right)
                return esq + dir + 1
        return 0

    def remove(self,data, root= -1):
        if root == -1:
            self.root = self.remove(data, self.root)
            return
        if root is not None:
            if data > root.data:
                root.right = self.remove(data, root.right)
            elif data < root.data:
                root.left = self.remove(data, root.left)

            if root.data == data:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return  root.left
                else:
                    root.data = self.menorSucessor(root.data, root.right)
                    root.right = self.remove(data, root.right)
            return root

    def menorSucessor(self, data, root=-1):
        if root == -1:
            return self.menorSucessor(data, root = self.root)
        if root is not None:
            if root.left is not None:
                return self.menorSucessor(data, root.left)
            else:
                aux = root.data
                root.data = data
                return aux

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
