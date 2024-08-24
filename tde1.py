def processar_operacoes(arquivo_entrada):
    #Abre o arquivo em modo de leitura
    with open(arquivo_entrada, 'r') as file:
        num_operacoes = int(file.readline().strip())

        #loop
        for i in range(num_operacoes):
            operacao = file.readline().strip()
            conjunto1 = set(file.readline().strip().split(', '))
            conjunto2 = set(file.readline().strip().split(', '))

            #Verifica a operação
            if operacao == 'U':
                resultado = conjunto1.union(conjunto2)
                print(f"União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
            elif operacao == 'I':
                resultado = conjunto1.intersection(conjunto2)
                print(f"Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
            elif operacao == 'D':
                resultado = conjunto1.difference(conjunto2)
                print(f"Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
            elif operacao == 'C':
                resultado = {(x, y) for x in conjunto1 for y in conjunto2}
                print(f"Produto Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
            #código desconhecido
            else:
                print("Operação desconhecida.")


#Exemplo de execução
#O input deixa o usuário escolher qual entrada de texto ele quer executar
arquivo_entrada = input("Digite o nome do arquivo de entrada (incluindo a extensão .txt): ")
processar_operacoes(arquivo_entrada)

