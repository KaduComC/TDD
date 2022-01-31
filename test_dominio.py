from unittest import TestCase

from dominio import Lance, Usuario, Leilao


class TestLeilao(TestCase):

    # isso define componentem em comum com outras classes
    # e já é chamado automaticamente sem precisar chamar
    # nas outras classes
    def setUp(self):
        self.gui = Usuario('Gui')
        self.yuri = Usuario('Yuri')
        self.kadu = Usuario('Kadu')

        self.lance2 = Lance(self.yuri, 150.0)
        self.lance1 = Lance(self.gui, 110.0)
        self.lance3 = Lance(self.kadu, 200.0)

        self.leilao = Leilao('Celular')

    def test_avalia_que_retorna_o_maior_e_o_menor_valor_em_ordem_crescente(self):
        self.leilao.propoe(self.lance1)
        self.leilao.propoe(self.lance2)

        menor_valor_esperado = 110.0
        maior_valor_esperado = 150.0

        # assetEqual() faz uma comparação. se for certo o programa passa
        # se for diferente o programa da erro
        # é preciso passar 2 parametros para avalição e um terceiro opcional
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_avalia_que_retorna_o_maior_e_o_menor_valor_em_ordem_decrescente(self):
        self.leilao.propoe(self.lance1)
        self.leilao.propoe(self.lance2)

        menor_valor_esperado = 110.0
        maior_valor_esperado = 150.0

        # assetEqual() faz uma comparação. se for certo o programa passa
        # se for diferente o programa da erro
        # é preciso passar 2 parametros para avalição e um terceiro opcional
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_avalia_que_retorna_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_tiver_um_lance(self):
        self.leilao.propoe(self.lance2)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_avalia_que_retorna_o_maior_e_o_menor_lance_quando_tiver_tres_lances(self):
        self.leilao.propoe(self.lance1)
        self.leilao.propoe(self.lance2)
        self.leilao.propoe(self.lance3)

        self.assertEqual(110.0, self.leilao.menor_lance)
        self.assertEqual(200.0, self.leilao.maior_lance)