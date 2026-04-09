# Weather ETL Pipeline

A Data Engineering project that implements an ETL (Extract, Transform, Load) pipeline to collect, process, and store real-time weather data.

## Overview

This project consumes data from a public weather API, processes and cleans the data, and stores the results in a local database, enabling the creation of historical datasets over time.

Pipeline flow:

```
API → Extract → Transform → Load → SQLite
```

## Features

* Data extraction from a weather API (Open-Meteo)
* Data cleaning, transformation, and structuring
* Data storage in a SQLite database
* Historical data persistence for future analysis

## Architecture

The project follows a simple and modular ETL architecture:

* Extract: HTTP requests to the API
* Transform: Data processing using Pandas
* Load: Data insertion into SQLite

## Technologies

* Python 3.x
* Pandas
* Requests
* SQLite

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the pipeline

```bash
python -m src.main
```
