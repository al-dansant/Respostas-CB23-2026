class Node:
    def __init__(self,item):
        '''
        Inicializa a classe Node.
        
        :param item: valor atribuído ao elemento da classe.

        Complexidade: O(1)
        '''
        self.valor = item
        self.proximo = None

    def __repr__(self):
        '''
        Define a representação textual do elemento da classe.

        Complexidade: O(1)
        '''
        return str(self.valor)

class PilhaEncadeada:
    def __init__(self):
        '''
        Inicializa a classe PilhaEncadeada.
        
        :param self: elemento da classe.

        Complexidade: O(1)
        '''
        self.head = Node(None)
        self.elements = 0

    def push(self,item):
        '''
        Adiciona um item na Pilha.
        
        :param item: valor a ser adicionado na pilha.

        Complexidade: O(1)
        '''
        new = Node(item)
        new.proximo = self.head
        self.head = new
        self.elements += 1

    def pop(self):
        '''
        Remove e retorna o item do topo da pilha.
        
        Complexidade: O(1)
        '''
        if self.elements == 0: 
            raise IndexError("A pilha está vazia")
        else:
            a = self.head
            self.head = self.head.proximo
            self.elements -= 1
            return a.valor
        
    def topo(self):
        '''
        Retorna o item do topo da pilha.
        
        Complexidade: O(1)
        '''
        if self.elements == 0: 
            raise IndexError("A pilha está vazia")
        else:
            return self.head.valor

    def esta_vazia(self):
        '''
        Retorna True se a pilha estiver vazia e False se houver elementos.
        
        Complexidade: O(1)
        '''
        if self.elements == 0: return True
        else: return False

    def __len__(self):
        '''
        Retorna a quantidade de elementos na pilha.
        
        Complexidade: O(1)
        '''
        return self.elements

    def __repr__(self):
        '''
        Define a representação textual da pilha.

        Complexidade: O(n)
        '''
        if self.head.valor is None: return "[]"
        else:
            b = self.head
            s = f"[{b.valor}"
            while b.proximo.valor is not None:
                b = b.proximo
                s = s + f", {b.valor}"
            return s + "]"
        
giga = PilhaEncadeada()
giga.push(12)
giga.push(13)
print(giga)
giga.push(14)
print(giga)
giga.pop()
print(giga)