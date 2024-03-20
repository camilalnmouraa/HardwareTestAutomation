class EmuladorNIUSB6001:
    
    def __init__(self, num_pinos_entrada=1, num_pinos_saida=1):
        self.num_pinos_entrada = num_pinos_entrada
        self.num_pinos_saida = num_pinos_saida
        self.pinos_entrada = [False] * num_pinos_entrada
        self.pinos_saida = [False] * num_pinos_saida

    def ativar_pino_saida(self, indice_pino):
        if indice_pino < self.num_pinos_saida:
            self.pinos_saida[indice_pino] = True

    def desativar_pino_saida(self, indice_pino):
        if indice_pino < self.num_pinos_saida:
            self.pinos_saida[indice_pino] = False

    def ler_estado_pino_entrada(self, indice_pino):
        if indice_pino < self.num_pinos_entrada:
            return self.pinos_entrada[indice_pino]
        else:
            return None

    def simular_mudanca_pino_saida(self, indice_pino):
        if indice_pino < self.num_pinos_saida:
            self.pinos_entrada[indice_pino] = self.pinos_saida[indice_pino]


if __name__ == "__main__":
    def exemplo_uso_emulador():
        emulador = EmuladorNIUSB6001(num_pinos_entrada=2, num_pinos_saida=2)

        # Ativa o primeiro pino de saída
        emulador.ativar_pino_saida(0)

        # Simula mudança no estado do primeiro pino de saída
        emulador.simular_mudanca_pino_saida(0)

        # Verifica o estado do primeiro pino de entrada
        estado_pino_entrada = emulador.ler_estado_pino_entrada(0)
        print("Estado do primeiro pino de entrada:", estado_pino_entrada)

        # Desativa o primeiro pino de saída
        emulador.desativar_pino_saida(0)

        # Simula outra mudança no estado do primeiro pino de saída
        emulador.simular_mudanca_pino_saida(0)

        # Verifica novamente o estado do primeiro pino de entrada
        estado_pino_entrada = emulador.ler_estado_pino_entrada(0)
        print("Estado do primeiro pino de entrada:", estado_pino_entrada)

    # Chamando a função de exemplo de uso do emulador
    exemplo_uso_emulador()