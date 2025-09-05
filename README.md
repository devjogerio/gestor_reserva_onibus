# Reserva de Passagens de Ônibus

Este projeto é uma aplicação Python com interface gráfica (Tkinter) para reserva de assentos em ônibus, utilizando padrão MVC.

## Estrutura do Projeto

- `app/model/`: Lógica de dados e manipulação das reservas.
- `app/controller/`: Intermediação entre interface e dados.
- `app/view/`: Interface gráfica (Tkinter).
- `Dados.xlsx`: Arquivo de dados das reservas (não versionado).

## Como executar

1. Instale as dependências:
   ```bash
   pip install openpyxl
   ```
2. Execute a interface:
   ```bash
   python app/view/view_onibus.py
   ```

## Observações
- O arquivo `Dados.xlsx` deve existir na raiz do projeto e conter uma planilha chamada `Reservas` com as colunas: Lugar, Nome, CPF, Data.
- O projeto está pronto para ser versionado no GitHub.
