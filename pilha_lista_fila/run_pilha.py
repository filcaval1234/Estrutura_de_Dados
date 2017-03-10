from pilha import *
p = pilha()
p.push(5)
p.push(3)
p.push(4)
p.push(1)
p.push(2)

p.ordena_pilha()
p.removerElem(0)
print(p.pop(), p.pop(), p.pop(), p.pop(), p.pop(), )
print(p.empty())