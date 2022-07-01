from unittest import  TestCase
from components import  run_application



class TestRunApplication(TestCase):

    def test_ciclo_excecucao_normal(self):

        saida_esperada = [(1, 3, 'N'), (5, 1, 'E')]
        xmax = 5
        ymax = 5
        movimentacoes = [
            {
                "posicao" : (1,2,"N"),
                "instrucao": "LMLMLMLMM"
            },
            {
                "posicao": (3, 3, "E"),
                "instrucao": "MMRMMRMRRM"
            },
        ]

        saida_real = run_application(xmax=xmax,ymax=ymax,movimentacoes=movimentacoes)

        self.assertEqual(saida_real,saida_esperada)


