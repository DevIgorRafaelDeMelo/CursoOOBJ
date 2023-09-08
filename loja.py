from higiene import higiene

class Loja:
    def __init__(self,nome , programa):
        self.nome = nome
        self._programas = programa

    def __getitem__(self,item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)