






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
