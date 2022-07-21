class NoDaLista:
    valor = 0
    proximo = None
    def __init__(self, valor):
        self.valor = valor

class ListaOrdenada:
    primeiro = None
    ultimo = None
    tamanho = 0
    def __init__(self):
        self.tamanho = 0
    
    def Adicionar(self, valor):
        NovoNo = NoDaLista(valor)
        if(self.primeiro == None and self.ultimo == None):
            self.primeiro = NovoNo
            self.ultimo = NovoNo
        else:
            self.ultimo.proximo = NovoNo
            self.ultimo = NovoNo
        self.tamanho = self.tamanho + 1


    def Pegar(self, valor):
        NovoNo = self.primeiro
        Contagem = 0
        while(True):
            if(Contagem == valor):
                return NovoNo
            else:
                NovoNo = NovoNo.proximo
            Contagem = Contagem + 1
    
    def Deletar(self, valor):
        NovoNo = self.primeiro
        Antecessor = None
        Contagem = 0
        while(True):
            if(Contagem == valor):
                break
            else:
                Antecessor = NovoNo
                NovoNo = NovoNo.proximo
            Contagem = Contagem + 1
        if NovoNo == self.primeiro:
            self.primeiro = NovoNo.proximo
            NovoNo = None
        else:
            Antecessor.proximo = NovoNo.proximo
            NovoNo = None
        self.tamanho = self.tamanho - 1
                
variavel = ListaOrdenada();
variavel.Adicionar(15)
variavel.tamanho
variavel.Adicionar(41)
variavel.Adicionar(2)
variavel.Adicionar(65)

variavel.Deletar(3)
x = 0
while(x < variavel.tamanho):
    print("Vetor {0}: {1}".format(x, variavel.Pegar(x).valor))
    x = x + 1

print("")