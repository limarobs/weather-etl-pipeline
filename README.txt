# Weather ETL Pipeline

Projeto de engenharia de dados que implementa um pipeline ETL consumindo dados de uma API de clima.

## Funcionalidades

- Extração de dados via API (Open-Meteo)
- Transformação e limpeza dos dados
- Armazenamento em banco SQLite
- Histórico de dados ao longo do tempo

## Arquitetura

API → Extract → Transform → Load → SQLite

## Tecnologias

- Python
- Pandas
- Requests
- SQLite

## Como rodar

```bash
pip install -r requirements.txt
python -m src.main
