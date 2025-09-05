"""
Arquivo: controller_onibus.py
Responsável por intermediar a comunicação entre a view (interface) e o model (dados).
"""

from app.model.model_onibus import Onibus

class OnibusController:
    def __init__(self, capacidade, caminho_arquivo):
        """
        Inicializa o controller, criando uma instância do modelo Onibus.
        """
        self.onibus = Onibus(capacidade, caminho_arquivo)

    def reservar(self, num_lugar, nome, cpf, dia):
        """
        Solicita ao modelo a reserva de um lugar.
        """
        return self.onibus.reservar_lugar(num_lugar, nome, cpf, dia)

    def cancelar(self, num_lugar, dia):
        """
        Solicita ao modelo o cancelamento de uma reserva.
        """
        return self.onibus.cancelar_reserva(num_lugar, dia)

    def mapa(self, dia):
        """
        Solicita ao modelo o carregamento das reservas e retorna o mapa de assentos.
        """
        self.onibus.carregar_reservas(dia)
        return self.onibus.gerar_mapa()
