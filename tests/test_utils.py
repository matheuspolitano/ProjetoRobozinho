from utils import SN_tratar
from unittest import TestCase
class TestSNTratar(TestCase):

    def test_SN_tratar_S(self):
        value = "S"
        self.assertEqual(SN_tratar(value),True)
    def test_SN_tratar_S(self):
        value = "N"
        self.assertEqual(SN_tratar(value),False)

    def test_SN_erro_value(self):
        erro_esperado = ValueError("Valor deve ser S ou N")
        value = "123123"
        erro_real = None
        try:
            SN_tratar(value)

        except ValueError as ve:
            erro_real = ve

        self.assertEqual(erro_real.args,erro_esperado.args)
