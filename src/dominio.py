from src.excecoes import Lance_Invlaido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_e_valido(valor):
            raise Lance_Invlaido('Não pode propor um lance con valor maior que o valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_e_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    # acessa os lances
    @property
    def lances(self):
        return self.__lances[:]  # copia rasa [:]

    def propoe(self, lance: Lance):
        if self._lance_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise Lance_Invlaido('O mesmo usuário não pode dar dois lances seguidos')

    def _valor_maior_que_lance_anterios(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise Lance_Invlaido('O valor do lance deve ser maior que o lance anterior')

    def _lance_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance) and
                                          self._valor_maior_que_lance_anterios(lance))
