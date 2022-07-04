




def leitor_arquivo(path:str) -> list:
    """
    Esta funcao ira ler um arquivo e devolver uma lista das linhas junto com uma lista dentro de cara palavra dividida com espaco

    Parameters
    --------

    path:str
        caminho do arquivo

    return list<list<str>>
        Retorna uma lista contendo outra lista, cada lista eh uma linha

    
    """

    info_arquivo = []
    with open(path,"r") as f:
        conteudo = f.read()
        #separar as linha
        linhas = conteudo.split("\n")
        for item_linha in linhas:
            # cada palavra sera um string dentro da lista
            # aqui sera retirar todos os espaco antes e depois das palavras  
            sep_espaco = [sep_item.strip() for sep_item in item_linha.split(" ") if sep_item.strip() ]
            if len(sep_espaco):
                info_arquivo.append(sep_espaco)

    return info_arquivo


def SN_tratar(value:str) -> bool:
    """
    Estã funcao vai receber S OU N e devolver True ou False


    Parameters
    ----------
    value:str
        (S/N)

    return: bool

    Exceptions

    * todo valor que não seja S ou N

    Exemplo:

    >>> value = "S"
    >>> (SN_tratar(value)
    True



    """
    value = value.upper()
    if not value in  ["S","N"]:
        raise  ValueError("Valor deve ser S ou N")

    if value =="S":
        return True


    return False
