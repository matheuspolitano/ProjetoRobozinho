from unittest import TestCase
from components import  Robozinho,direcoes


class TestRobozinho(TestCase):
    def test_direcao(self):
        # verificar se está aceitando direcao correta
        direcao = "W"
        robo = Robozinho(10,10,100,100,direcao,[])
        self.assertEqual(robo.direcao,direcao)
    def test_direcao_errada(self):
        # testa o erro
        direcao = "D"
        erro_esperado = ValueError("Valor deve ser uma dessas letras {}".format(",".join(direcoes)))
        erro_real = None
        try:
            Robozinho(10,10,100,100,direcao,[])

        except ValueError as ve:
            erro_real =  ve

        self.assertEqual(erro_esperado.args,erro_real.args)

    def test_y_fora_limite(self):
        y = 2000
        erro_esperado = ValueError("Valor de y fora dos limites")
        erro_real = None
        try:
            Robozinho(10, y, 100, 100, "W", [])

        except ValueError as ve:
            erro_real = ve

        self.assertEqual(erro_esperado.args, erro_real.args)

    def test_x_fora_limite(self):
        x = 2000
        erro_esperado = ValueError("Valor de x fora dos limites")
        erro_real = None
        try:
            Robozinho(x, 10, 100, 100, "W", [])

        except ValueError as ve:
            erro_real = ve

        self.assertEqual(erro_esperado.args, erro_real.args)

    def test_virar_esquerda(self):
        posicao_esperada = [10, 10, "N"]
        robo = Robozinho(10, 10, 100, 100, "W", [])
        robo.virar_esquerda()
        posicao_real = [robo.x,robo.y,robo.direcao]
        self.assertEqual(posicao_esperada,posicao_real)
    def test_virar_direita(self):
        posicao_esperada = [10, 10, "S"]
        robo = Robozinho(10, 10, 100, 100, "W", [])
        robo.virar_direita()
        posicao_real = [robo.x,robo.y,robo.direcao]
        self.assertEqual(posicao_esperada,posicao_real)

    def test_mov(self):
        posicao_esperada = [10, 9, "S"]
        robo = Robozinho(10, 10, 100, 100, "S", [])
        robo.mover()
        posicao_real = [robo.x,robo.y,robo.direcao]
        self.assertEqual(posicao_esperada,posicao_real)

    def test_mov_erro_mesmo_espaco(self):
        erro_esperado = Exception('Robos ocupando mesmo espaco!!')
        erro_real = None
        robo = Robozinho(10, 10, 100, 100, "S", [(10, 9)])
        try:
            robo.mover()
        except Exception as e:
            erro_real = e

        self.assertEqual(erro_real.args,erro_esperado.args)

    def test_mov_erro_fora_limite(self):
        erro_esperado = Exception('Fora dos limites!!')
        erro_real = None
        robo = Robozinho(100, 100, 100, 100, "N", [(10, 9)])
        try:
            robo.mover()
        except Exception as e:
            erro_real = e

        self.assertEqual(erro_real.args,erro_esperado.args)









