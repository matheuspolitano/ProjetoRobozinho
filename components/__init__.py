from utils import SN_tratar, leitor_arquivo


separacao = "".join(["-" for item in range(0, 10)])
direcoes = ['N', 'E', 'S', 'W']

move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

instructions = {'L': 'virar_direita', 'R': 'virar_esquerda', 'M': 'mover'}


class Robozinho:
    """
      A class é  para controlar o roboi

      ...

      Attributes
      ----------
      x : int
          Posicao no eixo x
      y : int
          Posicao no eixo y
      xmax : int
          Limite da posicao eixo x
      ymax : int
          Limite da posicao eixo y
      direcao : str
          Apenas uma letra e precisa ser uma dessas três 'N', 'E', 'S', 'W'

     outras_posicoes: list
            Lista de outras posicoes, para verificar se aquela posicao já esta ocupada


      """
    def __init__(self, x, y, xmax, ymax, direcao, outras_posicoes):
        self.xmax = xmax
        self.ymax = ymax
        self.outras_posicoes = set(outras_posicoes)
        self.direcao = direcao
        self.x = x
        self.y = y
        


    @property
    def direcao(self):
        return self._direcao

    @direcao.setter
    def direcao(self,value):
        if value not in direcoes:
            raise  ValueError("Valor deve ser uma dessas letras {}".format(",".join(direcoes)))
        self._direcao = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        if value > self.xmax:
            raise ValueError("Valor de x fora dos limites")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,value):
        if value > self.ymax:
            raise ValueError("Valor de y fora dos limites")
        self._y = value



    def virar_esquerda(self) -> None:
        """
        Está funcao ira virar a esquerda o robo
        """
        self.direcao = direcoes[(direcoes.index(self.direcao) + 1) % len(direcoes)]

    def virar_direita(self) -> None:
        """
        Está funcao ira virar a direita o robo
        """
        self.direcao = direcoes[(direcoes.index(self.direcao) - 1) % len(direcoes)]

    def mover(self) -> None:
        """
        Está funcao ira mover para frente o robo


        Exceptions

        * O robo não ocupa o lugar de outro robo
        * O robo não ultrapassa o limite
        """
        xmod = self.x + move[self.direcao][0]
        ymod = self.y + move[self.direcao][1]
        # check outras_posicoes to see if nrobo is not the same position as mrobo
        if (xmod, ymod) not in self.outras_posicoes:
            if xmod <= self.xmax and xmod >= 0:
                self.x = xmod
            if ymod <= self.ymax and ymod >= 0:
                self.y = ymod
            else:
                raise Exception('Fora dos limites!!')

        else:
            raise  Exception('Robos ocupando mesmo espaco!!')

def tratar_arquivo(path_arquivo:str):

    """
    Esta funcao ira ler o arquivo e tratar o dados para o padrao esperado no run application

    Parameters

    ----------

    path_arquivo: pasta do arquivo


    return: list
        list<int,int,list>

        retorna os dados capturados na linha de comando


    """

    conteudo_arquivo = leitor_arquivo(path_arquivo)
    qtd_linha = len(conteudo_arquivo)
    if qtd_linha  < 3:
        raise ValueError("O arquivo deve ter pelo menos tres linhas")
    if qtd_linha%2==0:
        raise ValueError("O arquivo deve ter sempre o numero impara de linhas, sendo a primeira linha os limite e o restante posicao do robo e intrucao")
    
    
    

    
    #capturar posicao inicial
    xmax,ymax= map(int,conteudo_arquivo[0])
    movimentacoes = []

    x, y, direcao =  conteudo_arquivo[1]
    

    

    qtd_robo = qtd_linha//2

    for index_robo in range(0,qtd_robo):
        index_linha_posicao_robo = (2*index_robo)+1
        index_linha_instrucao_robo = (2*index_robo)+2
        x,y, direcao = conteudo_arquivo[index_linha_posicao_robo]
        posicao = [int(x), int(y), str(direcao)]

        instrucao = conteudo_arquivo[index_linha_instrucao_robo][0]
        movimentacoes.append({"posicao": posicao, "instrucao":instrucao})
      
    return  (xmax,ymax,movimentacoes)

def input_manual():

    """
    Funcao para capturar dados de cada robo no proprio terminal

    return: list
        list<int,int,list>

        retorna os dados capturados na linha de comando


    """

    xmax,ymax= map(int,input("Determine tamanho maximo no eixo X e Y: \nExemplo: 100 100\n:").split())
    movimentacoes = []

    x, y, direcao =  input("Me diga a posicao que vc quer do robo no eixo x e y, assim como sua direcao(N/E/S/W): \nExemplo: 5 5 W\n Fique atento com\n* Não passar do limite\n* Não colocar dois robos na mesma posicao\n:").split()

    posicao = [int(x), int(y), str(direcao)]

    instrucao = input("Passe uma instrucao para o robo, cada letra é uma instrucao (L/R/M)\nDicionario\nL: virar para esquerda\nR: Virar para a direita\nM: Mover para frente\n*Pode se dar mais de uma comando por vez\nExemplo: MMRMMRMRRM\n:")

    movimentacoes.append({"posicao": posicao,  "instrucao":instrucao})

    adicionar_robo = SN_tratar(input("Você deseja adicionar outro robo (S/N):"))

    while adicionar_robo:
        x, y, direcao = input(
                    "Me diga a posicao que vc quer do robo no eixo x e y, assim como sua direcao(N/E/S/W):").split()
        posicao = [int(x), int(y), str(direcao)]

        instrucao = input(
                    "Passe uma instrucao para o robo, cada letra é uma instrucao (L/R/M):")
        movimentacoes.append({"posicao": posicao, "instrucao":instrucao})
        adicionar_robo = SN_tratar(input("Você deseja adicionar outro robo (S/N):"))
    return  (xmax,ymax,movimentacoes)

def capturar_dados_terminal() -> list:
    """
    Funcao para capturar dados para serem inseridos para roda run_application

    return: list
        list<int,int,list>

        retorna os dados capturados na linha de comando


    """

    print("Olá Bem vindo :)\n{separacao}".format(separacao=separacao))

    try:
        #verificar se vai ser adicionado por arquivo de texto
        por_arquivo_texto = SN_tratar(input("Você deseja adicionar via arquivo de texto (S/N):"))
        dados = None
        if por_arquivo_texto:
            path_arquivo = input("Me diga qual o caminho do arquivo \nExemplo ./tests_files/input_test.txt \n:")
            dados = tratar_arquivo(path_arquivo)

        else:
            dados =  input_manual()
        return dados

        

    except Exception as e:
        print("Erro encontrado..\n{separacao}".format(separacao=separacao))
        print(str(e))
        exit()


def mensagem_final_terminal(saida_run_process:list) -> None:
    """
    Funcao gera uma mensagem final para o usuario com os dados da saida da funcao run_process




    """

    print("Resultado dos {qnt_robo} robos\n{separacao}".format(qnt_robo=len(saida_run_process),separacao=separacao))

    for index,item_saida in enumerate(saida_run_process):
        if index==0:
            print("X | Y | Direção")
        print(" ".join(map(str,item_saida)))

    print("Muito Obrigadooo :)")


def run_application(xmax:int,ymax:int,movimentacoes:list)->list:
        """
            Executa comando para robos determinando suas posicoes e movimentando eles

           Parameters
           ----------
           xmax : int
                Limite da posicao eixo x

           ymax : int
                Limite da posicao eixo y

           movimentacoes : list<dict<posicao,instrucao>>
                lista de dict com posicao e intrucoes para o robo

            Return: list
                saida com as posicoes finais apos a movimentacoes


           Exceptions
           ------

           * Instrucao invalida
           * Posicão especificada já ocupada

           Exemple:

            >>>xmax = 5
            >>>ymax = 5
            >>>movimentacoes = [
                {
                    "posicao" : (1,2,"N"),
                    "instrucao": "LMLMLMLMM"
                },
                {
                    "posicao": (3, 3, "E"),
                    "instrucao": "MMRMMRMRRM"
                },
            ]

            >>>run_application(xmax=xmax,ymax=ymax,movimentacoes=movimentacoes)
            [(1, 3, 'N'), (5, 1, 'E')]




        """

        outras_posicoes = set([])
        verificar_coords = []
        saida = []
        count_a = 1
        count_b = 1
        # iterate over robo count
        for movimentacao_robo in movimentacoes:
            # pegar as posicoes
            x, y, direcao = movimentacao_robo["posicao"]
            count_a += 1

            if [x, y, direcao] not in verificar_coords:
                verificar_coords.append([x, y, direcao])
                robo = Robozinho(int(x), int(y), xmax, ymax, direcao, outras_posicoes)

                #rodar cada instrucao
                for i in movimentacao_robo["instrucao"]:
                    #verificar se a instrucao eh valida
                    if i not in 'MRL':
                        raise Exception ('Instrucao invalida precisa ser uma dessas {}'.format(",".join(instructions.keys())))
                    else:
                        # rodar instrucao
                        getattr(robo, instructions[i])()
                count_b += 1
                outras_posicoes.add((robo.x, robo.y))
                saida.append((robo.x, robo.y, robo.direcao))
            else:
                raise Exception("Existe mais de um robo ocupando o mesmo espaco")

        return saida


