from src.dominio import Leilao, Usuario

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance():
    vini = Usuario('Vini', 100.0)

    leilao = Leilao('Celular')

    vini.propoe.lance(Leilao, 50.0)

    assert vini.carteira == 50.0