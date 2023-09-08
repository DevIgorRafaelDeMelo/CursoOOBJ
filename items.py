from loja import Loja

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

for loja in mercado:
    print(loja)
