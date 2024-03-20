import sys
import os
import pytest
# Adiciona o diretório 'src' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
# Importa a classe EmuladorNIUSB6001
from emulador_ni_usb_6001 import EmuladorNIUSB6001

def test_ativar_e_desativar_pino_saida():
    emulador = EmuladorNIUSB6001(num_pinos_saida=2)
    
    # Ativa o primeiro pino de saída
    emulador.ativar_pino_saida(0)
    assert emulador.pinos_saida[0] == True
    
    # Desativa o segundo pino de saída
    emulador.desativar_pino_saida(1)
    assert emulador.pinos_saida[1] == False

def test_ler_estado_pino_entrada():
    emulador = EmuladorNIUSB6001(num_pinos_entrada=2)
    
    # Simula que o segundo pino de entrada está ativo
    emulador.pinos_entrada[1] = True
    estado_pino_entrada = emulador.ler_estado_pino_entrada(1)
    assert estado_pino_entrada == True

def test_simular_mudanca_pino_saida():
    emulador = EmuladorNIUSB6001(num_pinos_entrada=2, num_pinos_saida=2)
    
    # Ativa o primeiro pino de saída e simula mudança
    emulador.ativar_pino_saida(0)
    emulador.simular_mudanca_pino_saida(0)
    assert emulador.pinos_entrada[0] == True

    # Desativa o segundo pino de saída e simula mudança
    emulador.desativar_pino_saida(1)
    emulador.simular_mudanca_pino_saida(1)
    assert emulador.pinos_entrada[1] == False