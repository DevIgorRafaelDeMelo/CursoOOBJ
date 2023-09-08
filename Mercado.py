class Item:
    def __init__(self,idItem ,nome,valor,qtd):
        self._id = idItem
        self._nome = nome.title()
        self._valor = valor
        self._qtd = qtd

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor
    
    @property
    def qtd(self):
        return self._qtd
    
    def set_valor(self, valor):
        self._valor = valor

    def compra_item(self):
        if(self._qtd >= 1):
            self._qtd -= 1

    def repor_item(self):
        self._qtd + 1

    def __str__(self):
        return f'O Item: {self.nome} Do Valor de: {self.valor} Tem {self.qtd} un'

class Higiene(Item):
    def __init__(self,idItem, nome, valor, qtd):
        super().__init__(idItem, nome, valor, qtd)

class Loja:
    def __init__(self,nome , programa):
        self.nome = nome
        self._programas = programa

    def __getitem__(self,item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
    
    def valor_total(self):
        return self._programas

Cotonete = Higiene(1,"Cotonete",62.00, 40)
Pastadente = Higiene(2,"Pasta de dente",42.00, 340)
Shanpoo = Higiene(3,"Shanpoo",232.00, 50)
Rexonna = Higiene(4,"Rexonna",152.00, 640)
gel = Higiene(5,"gel",276.00, 60)
escovadente = Higiene(6,"escova de dente",234.00, 24)
laque = Higiene(7,"laque",222.00, 22)
papelhigienico = Higiene(8,"papel higienico",24.00, 12)
Condicionador = Higiene(9,"Condicionador",254.00, 75)
creme = Higiene(10,"creme",24.00, 240)
Fiodental = Higiene(11,"Fio dental",52.00, 540)

itens_de_higiene = [Cotonete,Pastadente,Shanpoo,Rexonna,gel,escovadente,laque,papelhigienico,Condicionador,creme,Fiodental]

mercado = Loja("Mercado um", itens_de_higiene )

Valor_total = 0

for loja in mercado:
    print(loja.valor)


