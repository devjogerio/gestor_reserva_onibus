"""
Arquivo: view_onibus.py
Responsável pela interface gráfica do usuário (GUI) usando tkinter.
"""


import tkinter as tk
from tkinter import ttk, messagebox
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
        self.root.geometry("480x700")
        self.root.configure(bg="#e9ecef")
        self.criar_widgets()


    def criar_widgets(self):
        """
        Cria e posiciona todos os widgets da interface (campos, botões, labels e área de texto).
        """
        ttk.Style().configure("TButton", font=("Arial", 13))
        ttk.Style().configure("TLabel", font=("Arial", 13))
        ttk.Style().configure("Title.TLabel", font=("Arial", 22, "bold"), background="#e9ecef")

        # Título
        ttk.Label(self.root, text="Reserva de Passagens", style="Title.TLabel").pack(pady=(18, 8))

        # Frame principal do formulário
        form_frame = ttk.Frame(self.root, padding=18, style="Card.TFrame")
        form_frame.pack(pady=(0, 10), padx=10, fill=tk.X)

        # Campos do formulário
        self.lugar_entry = self._criar_campo(form_frame, "Número do lugar:", 0)
        self.nome_entry = self._criar_campo(form_frame, "Nome:", 1)
        self.cpf_entry = self._criar_campo(form_frame, "CPF:", 2)
        self.dia_entry = self._criar_campo(form_frame, "Dia:", 3)
        self.dia_entry.insert(0, date.today().strftime("%d/%m/%Y"))

        # Botões
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=8)
        ttk.Button(btn_frame, text="Reservar", style="Accent.TButton", command=self.reservar).pack(side=tk.LEFT, padx=7)
        ttk.Button(btn_frame, text="Cancelar Reserva", command=self.cancelar).pack(side=tk.LEFT, padx=7)
        ttk.Button(btn_frame, text="Ver Mapa", command=self.ver_mapa).pack(side=tk.LEFT, padx=7)

        # Painel de status
        self.resultado_label = ttk.Label(self.root, text="", font=("Arial", 13), background="#e9ecef", foreground="#333")
        self.resultado_label.pack(pady=5)

        # Painel do mapa de assentos
        mapa_frame = ttk.LabelFrame(self.root, text="Mapa de Assentos", padding=12)
        mapa_frame.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)
        self.mapa_text = tk.Text(mapa_frame, width=48, height=12, font=("Consolas", 13), bg="#f8f9fa", fg="#222", relief=tk.FLAT, borderwidth=0)
        self.mapa_text.pack(fill=tk.BOTH, expand=True)

    def _criar_campo(self, frame, texto, linha):
        """
        Cria um campo de entrada (label + entry) para o formulário.
        """
        ttk.Label(frame, text=texto).grid(row=linha, column=0, sticky="e", pady=4, padx=2)
        entry = ttk.Entry(frame, font=("Arial", 13))
        entry.grid(row=linha, column=1, pady=4, padx=2)
        return entry

    def reservar(self):
        """
        Obtém os dados do formulário e solicita a reserva ao controller. Exibe o resultado na interface.
        Após reservar, limpa os campos para novo registro.
        """
        try:
            num_lugar = int(self.lugar_entry.get())
            nome = self.nome_entry.get()
            cpf = self.cpf_entry.get()
            dia = self.dia_entry.get()
            msg = self.controller.reservar(num_lugar, nome, cpf, dia)
            self._feedback(msg, sucesso="reservado" in msg)
            self.ver_mapa()
            self._limpar_campos()
        except Exception as e:
            self._feedback(f"Erro: {e}", sucesso=False)

    def _limpar_campos(self):
        """
        Limpa todos os campos do formulário após uma reserva.
        """
        self.lugar_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)
        self.dia_entry.delete(0, tk.END)
        self.dia_entry.insert(0, date.today().strftime("%d/%m/%Y"))

    def cancelar(self):
        """
        Obtém os dados do formulário e solicita o cancelamento ao controller. Exibe o resultado na interface.
        """
        try:
            num_lugar = int(self.lugar_entry.get())
            dia = self.dia_entry.get()
            msg = self.controller.cancelar(num_lugar, dia)
            self._feedback(msg, sucesso="cancelada" in msg)
            self.ver_mapa()
        except Exception as e:
            self._feedback(f"Erro: {e}", sucesso=False)

    def ver_mapa(self):
        """
        Solicita ao controller o mapa de assentos e exibe na área de texto.
        """
        dia = self.dia_entry.get()
        mapa = self.controller.mapa(dia)
        self.mapa_text.delete("1.0", tk.END)
        self.mapa_text.insert(tk.END, mapa)

    def _feedback(self, mensagem, sucesso=True):
        """
        Exibe feedback visual na label de status e destaca mensagens de sucesso ou erro.
        """
        cor = "#388e3c" if sucesso else "#d32f2f"
        self.resultado_label.config(text=mensagem, foreground=cor)
        if not sucesso:
            self.root.bell()

if __name__ == "__main__":
    root = tk.Tk()
    app = OnibusView(root)
    root.mainloop()
