from unittest import TestCase
from components import tratar_arquivo


class TestTratarArquivo(TestCase):

    def test_padrao(self):
        xmax_esperada = 5
        ymax_esperada = 5
        movimentacoes_esperada = [
            {
                "posicao" : [1,2,"N"],
                "instrucao": "LMLMLMLMM"
            },
            {
                "posicao": [3, 3, "E"],
                "instrucao": "MMRMMRMRRM"
            },
        ]
        path_file = "./tests_files/input_test.txt"
        xmax_real, ymax_real,movimentacoes_real = tratar_arquivo(path_file)

        self.assertEqual([xmax_esperada, ymax_esperada,movimentacoes_esperada],[xmax_real, ymax_real,movimentacoes_real])


