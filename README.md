# Sistema de Controle de Corridas de Táxi

Este é um sistema simples de controle de corridas de táxi, desenvolvido em Python usando a biblioteca Tkinter para a interface gráfica e o Pandas para a criação de planilhas Excel. O sistema permite registrar várias corridas, calcular o preço com base no bairro e gerar uma planilha com os dados de todas as corridas registradas. O programa foi desenvolvido para a cidade de João Pessoa (Paraíba), ou seja, os bairros e os preços estão já presetados. Ele foi feito para justamente otimizar o tempo de taxistas que precisam gerar planilhas de organização da empresa, com corridas, valor, local, número do vouncher, número do taxista e etc.

## Funcionalidades

- **Entrada de dados**: O usuário pode inserir informações sobre a origem da corrida, o bairro e o número do voucher, número do taxista.
- **Cálculo do preço**: O preço da corrida é calculado automaticamente com base no bairro informado. O preço de cada bairro é definido previamente no código.
- **Adição de várias corridas**: O sistema permite adicionar múltiplas corridas, uma de cada vez. Após cada entrada, o sistema limpa os campos de dados para que o usuário possa inserir a próxima corrida.
- **Geração de planilha**: Ao final, os dados de todas as corridas registradas são salvos em uma planilha Excel (formato `.xlsx`).

## Requisitos

- Python 3.x
- Bibliotecas Python necessárias:
  - `tkinter` (para interface gráfica)
  - `pandas` (para manipulação de dados e geração de planilhas Excel)
  - `geopy` (opcional, mas não é necessário no código atual, caso queira fazer com que apareça a distancia real em Km)
 
- Um Host
    - Esse programa posteriormente será gerado em Html, Css e Js para ter mais facilidade para dispositivos moveis e em todos os dispositivos em geral,

### Instalação das dependências

Para rodar este projeto, você precisará instalar as dependências. Você pode fazer isso usando o `pip`:


```bash
pip install pandas openpyxl
```

Todos os direitos reservados © Willian Teotonio 2024.




