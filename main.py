from dominio import Avaliador, Usuario, Lance, Leilao

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance1 = Lance(gui, 110.0)
lance2 = Lance(yuri, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance1)
leilao.lances.append(lance2)

for lance in leilao.lances:
    print(f'Usuário {lance.usuario.nome} deu um lance de {lance.valor}\n')

avaliador = Avaliador()
avaliador.avalia(leilao)
print(f'menor lance: {avaliador.menor_lance}\nmaior lance: {avaliador.maior_lance}')