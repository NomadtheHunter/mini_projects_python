while True:
    try:
        Capital = float(input("Capital: "))
        juros = float(input("Taxa de juros(inserir como 0,01 para 1% ou 0,008 para 0,8%): "))
        Tempo = float(input("Tempo: "))

        Montante = Capital * ((1 + juros)**Tempo)
        print("Montante: ", Montante)
        break

    except ValueError:
        print("Erro: Por favor, insira um valor valido.")