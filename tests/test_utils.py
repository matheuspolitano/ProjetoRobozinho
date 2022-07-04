from utils import SN_tratar,leitor_arquivo
from  os import remove
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


class LeitorArquivo(TestCase):

    def test_leitor_arquivo(self):
        #criando arquivo para testar o leitor
        content_file = "12 12 12\n12        123122131223"
        path_file = "./tests_files/file_test_leito_arquivo.txt"
        with open(path_file,"w") as f:
            f.write(content_file)
        retorno_esperado= [["12","12","12"],["12","123122131223"]]
        retorno_real = leitor_arquivo(path_file)
        remove(path_file)
        self.assertEqual(retorno_real,retorno_esperado)

