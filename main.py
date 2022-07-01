from components import capturar_dados_terminal,run_application,mensagem_final_terminal



if __name__ == "__main__":
    dados_capturados = capturar_dados_terminal()
    saida =  run_application(*dados_capturados)
    mensagem_final_terminal(saida)

