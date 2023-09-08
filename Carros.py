class Veiculo:
    def __init__(self,  cor, km, ano):
        self._cor = cor
        self._ano = ano
        self._km = km
        self._velocidade = 0
    @property
    def cor(self):
        return self._cor
        
    @property
    def ano(self):
        return self._ano
        
    @property
    def km(self):
        return self._km

    @property
    def Kmh(self):
        return self._velocidade

    def acelerar_carro(self):
        self._velocidade += 1

    def reduzir_carro(self):
        if(self._velocidade >= 1):
            self._velocidade -= 1
        

class Carro(Veiculo):
    def __init__(self,modelo, cor, ano, km ):
        super().__init__(cor, ano , km )
        self.modelo = modelo
        

    def __str__(self):
        return f'modelo: {self.modelo} Cor: {self.cor} ano: {self.ano} '


class Loja:
    def __init__(self,nome , programa):
        self.nome = nome
        self._programas = programa

    def __getitem__(self,item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)


m220 = Carro("M220",'azul',20000,2011)
clio = Carro('Clio','Branco',231000,2010)
mazda = Carro('mazda','preto',12000,2001)
corsa = Carro('corsa','roxo',1000,2000)


Consecioneria = [clio, mazda, m220, corsa]
LogaUm = Loja("Loja de itajai", Consecioneria)



print(f'Filial Um :{len(LogaUm)} Veiculos disponiveis')



