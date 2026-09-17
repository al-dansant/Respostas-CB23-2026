import importlib 
modulo = "P06_3494_pilha_encadeada"
meu_modulo = importlib.import_module(modulo)

class FilaEncadeada:
    def __init__(self):
        '''
        Inicializa a classe FilaEncadeada.
        
        Compplexidade: O(1)
        '''
        self.entrada = meu_modulo.PilhaEncadeada()
        self.saida = meu_modulo.PilhaEncadeada()
        self.elements = 0

    def enfileirar(self, item):
        '''
        Adiciona um item no fim da fila.
        
        :param item: item a ser adicionado.

        Complexidade: O(1)
        '''
        self.entrada.push(item)
        self.elements += 1

    def frente(self):
        '''
        Retorna o item da frente da fila.
        
        Complexidade: O(1) Amortizada (caso médio).
        '''
        if self.elements == 0:
            raise IndexError("A fila está vazia")
        
        if self.saida.esta_vazia() is True:
            while self.entrada.esta_vazia() is False:
                self.saida.push(self.entrada.pop())
        
        return self.saida.head.valor

    def desenfileirar(self):
        '''
        Retorna o item da frente da fila e o remove.

        Complexidade: O(n) amortizada (caso médio).
        '''
        valor = self.frente()
        self.saida.pop()
        self.elements -= 1
        return valor
        
    def esta_vazia(self):
        '''
        Retorna True se a fila estiver vazia e False se houver elementos.
        
        Complexidade: O(1)
        '''
        if self.elements == 0: 
            return True
        else: 
            return False

    def __len__(self):
        '''
        Retorna a quantidade de elementos na fila.
        
        Complexidade: O(1)
        '''
        return self.elements
    
    def __repr__(self):
        '''
        Define a representação textual da fila.

        Complexidade: O(n)
        '''
        if self.saida.head.valor is not None:
            b = self.saida.head
            s = f"{b.valor}"
            while b.proximo.valor is not None:
                b = b.proximo
                s = s + f", {b.valor}"
        if self.entrada.head.valor is not None:
            a = self.entrada.head
            m = f"{a.valor}"
            while a.proximo.valor is not None:
                a = a.proximo
                m = f"{a.valor}, " + m
        if self.saida.head.valor is not None and self.entrada.head.valor is not None: 
            return f"[{s}, {m}]"
        if self.saida.head.valor is not None and self.entrada.head.valor is None: 
            return f"[{s}]"
        if self.saida.head.valor is None and self.entrada.head.valor is not None: 
            return f"[{m}]"
        if self.saida.head.valor is None and self.entrada.head.valor is None: 
            return f"[]"

giga = FilaEncadeada()

giga.enfileirar(12)
giga.enfileirar(13)
giga.enfileirar(14)
giga.enfileirar(15)
print(giga)
print(giga.frente())
giga.desenfileirar()

print(giga.frente())
print(giga)
