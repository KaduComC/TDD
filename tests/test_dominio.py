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

        self.lance1 = Lance(self.gui, 110.0)
        self.lance2 = Lance(self.yuri, 150.0)
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

    def test_avalia_que_nao_deve_permitir_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance2)
            self.leilao.propoe(self.lance1)

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

    # se o leilao não tiver lance, deve permitir propor um lance
    def teste_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lance(self):
        self.leilao.propoe(self.lance1)

        quantidade_de_lance = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lance)

    # se o ultimo usuario for difernete, deve permitir propor o lance
    def test_deve_permitir_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        cadu = Usuario('Cadu')
        lance4 = Lance(cadu, 250.0)

        self.leilao.propoe(self.lance1)
        self.leilao.propoe(lance4)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    # se o ultimo usuario for o mesmo, nao deve permitir propor o lance
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance1_1 = Lance(self.gui, 300.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance1)
            self.leilao.propoe(lance1_1)
            # quantidade_de_lance = len(self.leilao.lances)
            # self.assertEqual(1, quantidade_de_lance)