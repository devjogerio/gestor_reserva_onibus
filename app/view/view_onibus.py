"""
Arquivo: view_onibus.py
Responsável pela interface gráfica do usuário (GUI) usando tkinter.
"""

import tkinter as tk
from tkinter import ttk
from datetime import date
from app.controller.controller_onibus import OnibusController

CAMINHO_ARQUIVO = "Dados.xlsx"  # Caminho relativo para o arquivo de dados
CAPACIDADE_ONIBUS = 20


class OnibusView:
    def __init__(self, root):
        """
        Inicializa a interface gráfica, configura a janela principal e cria os widgets.
        """
        self.controller = OnibusController(CAPACIDADE_ONIBUS, CAMINHO_ARQUIVO)
        self.root = root
        self.root.title("Reserva de Passagens")
        self.root.geometry("420x800")
        self.root.configure(bg="#f5f5f5")
        self.criar_widgets()

    def criar_widgets(self):
        """
        Cria e posiciona todos os widgets da interface (campos, botões, labels e área de texto).
        """
        tk.Label(self.root, text="Reserva de Passagens", font=("Arial", 20, "bold"), bg="#f5f5f5").pack(pady=10)
        frame = tk.Frame(self.root, bg="#f5f5f5")
        frame.pack(pady=10)

        # Campos do formulário
        self.lugar_entry = self._criar_campo(frame, "Número do lugar:", 0)
        self.nome_entry = self._criar_campo(frame, "Nome:", 1)
        self.cpf_entry = self._criar_campo(frame, "CPF:", 2)
        self.dia_entry = self._criar_campo(frame, "Dia:", 3)
        self.dia_entry.insert(0, date.today().strftime("%d/%m/%Y"))

        # Botões
        btn_frame = tk.Frame(self.root, bg="#f5f5f5")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Reservar", font=("Arial", 14), bg="#4caf50", fg="white", command=self.reservar).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancelar Reserva", font=("Arial", 14), bg="#f44336", fg="white", command=self.cancelar).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Ver Mapa", font=("Arial", 14), bg="#2196f3", fg="white", command=self.ver_mapa).pack(side=tk.LEFT, padx=5)

        # Resultado
        self.resultado_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#f5f5f5")
        self.resultado_label.pack(pady=5)

        # Mapa
        self.mapa_text = tk.Text(self.root, width=50, height=10, font=("Arial", 14), bg="#fff")
        self.mapa_text.pack(pady=10)

    def _criar_campo(self, frame, texto, linha):
        """
        Cria um campo de entrada (label + entry) para o formulário.
        """
        tk.Label(frame, text=texto, font=("Arial", 14), bg="#f5f5f5").grid(row=linha, column=0, sticky="e", pady=2)
        entry = tk.Entry(frame, font=("Arial", 14))
        entry.grid(row=linha, column=1, pady=2)
        return entry

    def reservar(self):
        """
        Obtém os dados do formulário e solicita a reserva ao controller. Exibe o resultado na interface.
        """
        try:
            num_lugar = int(self.lugar_entry.get())
            nome = self.nome_entry.get()
            cpf = self.cpf_entry.get()
            dia = self.dia_entry.get()
            msg = self.controller.reservar(num_lugar, nome, cpf, dia)
            self.resultado_label.config(text=msg)
            self.ver_mapa()
        except Exception as e:
            self.resultado_label.config(text=f"Erro: {e}")

    def cancelar(self):
        """
        Obtém os dados do formulário e solicita o cancelamento ao controller. Exibe o resultado na interface.
        """
        try:
            num_lugar = int(self.lugar_entry.get())
            dia = self.dia_entry.get()
            msg = self.controller.cancelar(num_lugar, dia)
            self.resultado_label.config(text=msg)
            self.ver_mapa()
        except Exception as e:
            self.resultado_label.config(text=f"Erro: {e}")

    def ver_mapa(self):
        """
        Solicita ao controller o mapa de assentos e exibe na área de texto.
        """
        dia = self.dia_entry.get()
        mapa = self.controller.mapa(dia)
        self.mapa_text.delete("1.0", tk.END)
        self.mapa_text.insert(tk.END, mapa)

if __name__ == "__main__":
    root = tk.Tk()
    app = OnibusView(root)
    root.mainloop()
